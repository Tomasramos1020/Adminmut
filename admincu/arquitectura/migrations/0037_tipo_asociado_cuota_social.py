# Generated by Django 2.2.19 on 2023-11-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0036_auto_20231023_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_asociado',
            name='cuota_social',
            field=models.BooleanField(default=True),
        ),
    ]
