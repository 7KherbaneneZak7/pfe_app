# Generated by Django 4.0.4 on 2022-05-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_alter_candidat_group_sanguin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriepermi',
            name='nom',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]