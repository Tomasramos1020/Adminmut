# Generated by Django 2.2.19 on 2023-10-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0030_auto_20231021_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_mutual',
            name='nombre_reglamento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
