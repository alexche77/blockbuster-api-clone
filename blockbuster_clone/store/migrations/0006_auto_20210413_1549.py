# Generated by Django 3.1.8 on 2021-04-13 15:49

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0005_auto_20210413_0816"),
        ("store", "0005_remove_rentrequest_penalty_fee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "movement_type",
                    models.IntegerField(
                        choices=[
                            (1, "Sale"),
                            (2, "Rent"),
                            (3, "Rent Return"),
                            (4, "Defective Return"),
                            (5, "Purchase"),
                            (6, "Adjustment"),
                        ]
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                ("comments", models.CharField(max_length=255)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.00"))
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="movies.movie"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("movie_purchase", models.ManyToManyField(to="store.Movement")),
            ],
        ),
        migrations.RemoveField(
            model_name="inventoryadjustment",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="inventoryadjustment",
            name="user",
        ),
        migrations.RemoveField(
            model_name="purchase",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="purchase",
            name="user",
        ),
        migrations.RemoveField(
            model_name="rentrequest",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="rentrequest",
            name="user",
        ),
        migrations.RemoveField(
            model_name="rentreturn",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="rentreturn",
            name="user",
        ),
        migrations.RemoveField(
            model_name="sale",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="sale",
            name="user",
        ),
        migrations.DeleteModel(
            name="DefectiveReturn",
        ),
        migrations.DeleteModel(
            name="InventoryAdjustment",
        ),
        migrations.DeleteModel(
            name="Purchase",
        ),
        migrations.DeleteModel(
            name="RentRequest",
        ),
        migrations.DeleteModel(
            name="RentReturn",
        ),
        migrations.DeleteModel(
            name="Sale",
        ),
    ]
