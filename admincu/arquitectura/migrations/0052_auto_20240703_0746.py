# Generated by Django 2.2.19 on 2024-07-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0051_auto_20240613_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='acreedor',
            name='condicion_iva',
            field=models.CharField(blank=True, choices=[('iva_responsable_inscripto', 'IVA Responsable Inscripto'), ('iva_responsable_no_inscripto', 'IVA Responsable no Inscripto'), ('iva_no_responsable', 'IVA no Responsable'), ('iva_sujeto_exento', 'IVA Sujeto Exento'), ('responsable_monotributo', 'Responsable Monotributo'), ('sujeto_no_categorizado', 'Sujeto no Categorizado'), ('proveedor_exterior', 'Proveedor del Exterior'), ('iva_liberado', 'IVA Liberado Ley Nº 19.640'), ('iva_ri_ap', 'IVA Responsable Inscripto Agente de Percepción'), ('iva_ri_ap', 'IVA Responsable Inscripto Agente de Percepción')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='acreedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
