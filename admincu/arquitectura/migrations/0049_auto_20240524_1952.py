# Generated by Django 2.2.19 on 2024-05-24 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0048_socio_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='nombre',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
    ]
