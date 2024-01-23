# Generated by Django 2.0.3 on 2018-10-30 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CajaComprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(blank=True, max_length=10, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('capital', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('int_desc', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compensacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('numero', models.PositiveIntegerField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='compensacion/pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('confirmado', models.BooleanField(default=False)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='comprobantes/pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('compensacion_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saldos_utilizados', to='comprobantes.Compensacion')),
                ('comprobante_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saldos_utilizados', to='comprobantes.Comprobante')),
                ('comprobante_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saldos', to='comprobantes.Comprobante')),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]
