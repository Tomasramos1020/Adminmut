# Generated by Django 2.2.19 on 2022-05-09 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0018_auto_20220506_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio_mutual',
            name='grupo_asociados',
        ),
        migrations.AddField(
            model_name='servicio_mutual',
            name='socio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicios_mutuales', to='arquitectura.Socio'),
        ),
    ]
