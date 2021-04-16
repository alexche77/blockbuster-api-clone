# Generated by Django 3.1.8 on 2021-04-13 16:19

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_auto_20210413_1549"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movement",
            old_name="price",
            new_name="cost",
        ),
        migrations.AddField(
            model_name="movement",
            name="profit",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
    ]
