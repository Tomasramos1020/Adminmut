# Generated by Django 2.0.3 on 2018-12-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditos', '0005_liquidacion_mails'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='detalle',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
