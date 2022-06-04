# Generated by Django 4.0.4 on 2022-05-26 09:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compte', '0015_alter_candidat_date_de_dossier_alter_candidat_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='date_de_dossier',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 11, 46, 13, 120205)),
        ),
        migrations.AlterField(
            model_name='dwsr',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]