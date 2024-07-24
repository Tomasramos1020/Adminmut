# Generated by Django 2.2.19 on 2024-06-13 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0050_convenio'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='convenio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socio', to='arquitectura.Convenio'),
        ),
        migrations.AlterField(
            model_name='convenio',
            name='observaciones',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='convenio',
            name='reglamento',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]