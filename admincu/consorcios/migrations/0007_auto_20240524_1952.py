# Generated by Django 2.2.19 on 2024-05-24 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consorcios', '0006_consorcio_es_federacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consorcio',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='consorcio',
            name='nombre_completo',
            field=models.CharField(max_length=250),
        ),
    ]