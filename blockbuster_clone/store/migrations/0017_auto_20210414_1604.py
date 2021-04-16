# Generated by Django 3.1.8 on 2021-04-14 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0016_auto_20210414_1531"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="movements",
        ),
        migrations.AddField(
            model_name="movement",
            name="order",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="store.order",
            ),
            preserve_default=False,
        ),
    ]
