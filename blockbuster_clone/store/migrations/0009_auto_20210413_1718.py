# Generated by Django 3.1.8 on 2021-04-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_auto_20210413_1643"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movement",
            name="comments",
            field=models.CharField(default=None, max_length=255),
        ),
    ]
