# Generated by Django 3.1.8 on 2021-04-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210413_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='info',
            field=models.JSONField(default=dict, verbose_name='Movie information'),
        ),
    ]
