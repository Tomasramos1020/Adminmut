# Generated by Django 2.2.19 on 2024-01-15 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consorcios', '0005_consorcio_matricula'),
        ('proveeduria', '0003_auto_20240115_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('consorcio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consorcios.Consorcio')),
            ],
        ),
    ]
