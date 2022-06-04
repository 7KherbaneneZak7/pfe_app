# Generated by Django 4.0.4 on 2022-05-23 14:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compte', '0006_candidat_age_alter_candidat_date_de_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='date_de_dossier',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 16, 12, 56, 63452)),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]