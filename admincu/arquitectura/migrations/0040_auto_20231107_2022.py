# Generated by Django 2.2.19 on 2023-11-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0039_auto_20231107_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='estado',
            field=models.CharField(choices=[('vigente', 'Vigente'), ('baja', 'Baja'), ('suspendido', 'Suspendido')], default='vigente', max_length=20),
        ),
    ]
