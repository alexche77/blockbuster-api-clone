# Generated by Django 3.1.8 on 2021-04-13 07:02

from decimal import Decimal

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RentReturn",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RentRequest",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "penalty_fee",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=5
                    ),
                ),
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Purchase",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="InventoryAdjustment",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("reason", models.CharField(max_length=255)),
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
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DefectiveReturn",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("reason", models.CharField(max_length=255)),
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
            options={
                "abstract": False,
            },
        ),
    ]
