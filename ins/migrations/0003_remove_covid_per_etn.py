# Generated by Django 3.2.2 on 2021-05-08 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ins', '0002_auto_20210508_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covid',
            name='per_etn',
        ),
    ]
