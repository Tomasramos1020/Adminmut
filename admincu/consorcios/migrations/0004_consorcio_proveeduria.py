# Generated by Django 2.2.19 on 2023-11-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consorcios', '0003_consorcio_cuit_nasociado'),
    ]

    operations = [
        migrations.AddField(
            model_name='consorcio',
            name='proveeduria',
            field=models.BooleanField(default=False),
        ),
    ]
