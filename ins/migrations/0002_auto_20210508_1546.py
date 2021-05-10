# Generated by Django 3.2.2 on 2021-05-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='ciudad_municipio_nom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='departamento',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='departamento_nom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='edad',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='estado',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fecha_de_notificaci_n',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fecha_diagnostico',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fecha_inicio_sintomas',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fecha_muerte',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fecha_recuperado',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fuente_tipo_contagio',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='nom_grupo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='pais_viajo_1_cod',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='pais_viajo_1_nom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='per_etn',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='recuperado',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='sexo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='tipo_recuperacion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='ubicacion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='unidad_medida',
            field=models.PositiveIntegerField(null=True),
        ),
    ]