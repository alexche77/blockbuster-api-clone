# Generated by Django 3.1.8 on 2021-04-13 07:09

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_auto_20210413_0706"),
    ]

    operations = [
        migrations.AlterField(
            model_name="defectivereturn",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="defectivereturn",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="inventoryadjustment",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="inventoryadjustment",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="purchase",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="purchase",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="rentrequest",
            name="penalty_fee",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="rentrequest",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="rentrequest",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="rentreturn",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="rentreturn",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]