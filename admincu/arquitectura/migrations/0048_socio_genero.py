# Generated by Django 2.2.19 on 2024-05-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0047_auto_20240425_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='genero',
            field=models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('no_binario', 'No Binario'), ('otro', 'Otro')], max_length=30, null=True),
        ),
    ]
