# Generated by Django 4.0.4 on 2022-05-25 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0012_epreuve_examinateur_alter_candidat_date_de_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='date_de_dossier',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 16, 21, 29, 898588)),
        ),
        migrations.AlterField(
            model_name='epreuve',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]