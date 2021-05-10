from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sodapy import Socrata
import datetime
import numpy as np
from .models import covid
import json
from django.http import JsonResponse

# Create your views here.

# Convert to pandas DataFrame
#df = pd.DataFrame.from_records(results)

def getDataFromApi(request):
    if request.method == 'GET':
        client = Socrata("www.datos.gov.co", None)

        # filtro indígenas cantidad max 50.000
        results = client.get("gt2j-8ykr", limit=50000, per_etn_="1")

        # print(results[0])

        # transformar json a Panda DataFrame
        df = pd.DataFrame.from_records(results)

        #elimina columnas innecesarias
        df.drop(columns=['fecha_reporte_web', 'id_de_caso', 'per_etn_'], inplace=True)

        #renombra columnas
        df.rename(columns={'nom_grupo_': 'nom_grupo'}, inplace=True)

        # convierte texto a enteros
        for col in ['departamento', 'ciudad_municipio', 'edad','unidad_medida','pais_viajo_1_cod']:
            df[col] = df[col].fillna(-1).astype(int).replace(-1, None)

        # convierte texto a fechas
        for col in ['fecha_de_notificaci_n','fecha_inicio_sintomas','fecha_diagnostico','fecha_recuperado','fecha_muerte']:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df[col] = df.where(df[col].notnull(), None)

        # convierte nat y nan a None
        df = df.where(pd.notnull(df), None)

        #elimina los fallecidos erroneos
        df = df[df.recuperado != 'fallecido']

        #elimina los N/A
        df = df[df.recuperado != 'N/A']

        #elimina Barranquilla
        df = df[df.departamento_nom != 'BARRANQUILLA']

        #elimina Barranquilla
        df = df[df.departamento_nom != 'CARTAGENA']

        #elimina Barranquilla
        df = df[df.departamento_nom != 'STA MARTA D.E.']

        print ('borro registros db')
        # elimino todos los registros de la tabla covid
        covid.objects.all().delete()

        print ('insertando en db...')

        # inserto datos en db
        for idx, dic in enumerate(df.to_dict(orient='records')):
            try:
                # print(idx)
                registro =  covid()
                registro.fecha_de_notificaci_n = dic['fecha_de_notificaci_n']
                registro.departamento = dic['departamento']
                registro.departamento_nom = dic['departamento_nom']
                registro.ciudad_municipio = dic['ciudad_municipio']
                registro.ciudad_municipio_nom = dic['ciudad_municipio_nom']
                registro.edad = dic['edad']
                registro.unidad_medida = dic['unidad_medida']
                registro.sexo = dic['sexo']
                registro.fuente_tipo_contagio = dic['fuente_tipo_contagio']
                registro.ubicacion = dic['ubicacion']
                registro.estado = dic['estado']
                registro.pais_viajo_1_cod = dic['pais_viajo_1_cod']
                registro.pais_viajo_1_nom = dic['pais_viajo_1_nom']
                registro.recuperado = dic['recuperado']
                registro.fecha_inicio_sintomas = dic['fecha_inicio_sintomas']
                registro.fecha_diagnostico = dic['fecha_diagnostico']
                registro.fecha_recuperado = dic['fecha_recuperado']
                registro.tipo_recuperacion = dic['tipo_recuperacion']
                registro.nom_grupo = dic['nom_grupo']
                registro.fecha_muerte = dic['fecha_muerte']
                registro.save()

            except:
                print(idx, dic)
                continue

        print("Done")

        return HttpResponse(status=200)
    return HttpResponse(status=403)

def getIndigenas(request):
    if request.method == 'GET':
        departamento = request.GET.get('departamento', None)
        poblacion = request.GET.get('poblacion', None)

        if departamento is None:
            if poblacion is None:
                lista = list(covid.objects.all().values('departamento_nom', 'ciudad_municipio_nom', 'edad', 'sexo', 'fuente_tipo_contagio', 'recuperado', 'pais_viajo_1_nom', 'tipo_recuperacion', 'nom_grupo', 'fecha_muerte'))
            else:
                poblacion = poblacion.upper()
                lista = list(covid.objects.filter(nom_grupo=poblacion).values('departamento_nom', 'ciudad_municipio_nom', 'edad', 'sexo', 'fuente_tipo_contagio', 'recuperado', 'pais_viajo_1_nom', 'tipo_recuperacion', 'nom_grupo', 'fecha_muerte'))
        else:
            departamento = departamento.upper()
            if poblacion is None:
                lista = list(covid.objects.filter(departamento_nom=departamento).values('departamento_nom', 'ciudad_municipio_nom', 'edad', 'sexo', 'fuente_tipo_contagio', 'recuperado', 'pais_viajo_1_nom', 'tipo_recuperacion', 'nom_grupo', 'fecha_muerte'))
            else:
                poblacion = poblacion.upper()
                lista = list(covid.objects.filter(departamento_nom=departamento, nom_grupo=poblacion).values('departamento_nom', 'ciudad_municipio_nom', 'edad', 'sexo', 'fuente_tipo_contagio', 'recuperado', 'pais_viajo_1_nom', 'tipo_recuperacion', 'nom_grupo', 'fecha_muerte'))
        
        df = pd.DataFrame(lista)
        #print(df)

        #logica para sexo
        sexo = df.groupby(by=['recuperado', 'sexo'])['sexo'].count().to_frame().unstack(level=0).to_dict()
        s = {}
        for key in sexo.keys():
            s[key[1]] = sexo[key]
        print(s)
        
        #logica para tipo contagio
        tipoContagio = df.groupby(by=['recuperado', 'fuente_tipo_contagio'])['fuente_tipo_contagio'].count().to_frame().unstack(level=0).to_dict()
        tc = {}
        for key in tipoContagio.keys():
            tc[key[1]] = tipoContagio[key]
        
        print(tc)

        #logica para tipo recuperación
        tipoRecuperacion = df.groupby(by=['recuperado', 'tipo_recuperacion'])['tipo_recuperacion'].count().to_frame().unstack(level=0).to_dict()
        tr = {}
        for key in tipoRecuperacion.keys():
            tr[key[1]] = tipoRecuperacion[key]
        
        print(tr)

        #logica para datos por departamento
        estadoPorDepto = df.groupby(by=['departamento_nom', 'recuperado'])['recuperado'].count().to_frame().unstack(level=0).to_dict()
        epd = {}
        for key in estadoPorDepto.keys():
            epd[key[1]] = estadoPorDepto[key]
        
        print(epd)

        #return JsonResponse(data, safe=False)
        return JsonResponse({
            'sexo': str(s),
            'tipoContagio': str(tc),
            'tipoRecuperacion': str(tr),
            'epd': str(epd)
        }, safe=False)
    return HttpResponse(status=403)

def getDepartamentos(request):
    if request.method == 'GET':

        lista = covid.objects.values_list('departamento_nom', flat=True).distinct()
        listaOrdenada = str(sorted(list(lista)))
        #print(type(listaOrdenada))
        #print(listaOrdenada)
        
        return JsonResponse(listaOrdenada, safe=False)
    return HttpResponse(status=403)

def getGrupos(request):
    if request.method == 'GET':
        departamento = request.GET.get('departamento', None)

        print(departamento)

        if departamento is None:
            lista = covid.objects.values_list('nom_grupo', flat=True).distinct()
        else:
            departamento = departamento.upper()
            lista = covid.objects.filter(departamento_nom=departamento).values_list('nom_grupo', flat=True).distinct()
        
        listaOrdenada = str(list(lista))

        #return HttpResponse(listaOrdenada)
        return JsonResponse(listaOrdenada, safe=False)
    return HttpResponse(status=403)

        #     df = pd.DataFrame(list(covid.objects.get(
        #     Q(departamento_nom__startswith=departamento) | Q(nom_grupo__startswith=poblacion)
        # ).values('departamento_nom', 'ciudad_municipio_nom', 'edad', 'fuente_tipo_contagio', 'recuperado', 'pais_viajo_1_nom', 'tipo_recuperacion', 'nom_grupo', 'fecha_muerte')[:50]))

