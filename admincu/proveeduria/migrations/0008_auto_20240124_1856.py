# Generated by Django 2.2.19 on 2024-01-24 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consorcios', '0005_consorcio_matricula'),
        ('proveeduria', '0007_auto_20240124_1856'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NotasPedido',
            new_name='Notas_Pedido',
        ),
    ]
