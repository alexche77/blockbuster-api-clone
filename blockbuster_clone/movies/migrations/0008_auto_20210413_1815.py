# Generated by Django 3.1.8 on 2021-04-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0011_auto_20210413_1815"),
        ("movies", "0007_auto_20210413_1649"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="movements",
            field=models.ManyToManyField(
                related_name="movie_movements", to="store.Movement"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="base_price_policy",
            field=models.IntegerField(
                choices=[(1, "AVERAGE"), (2, "HIGHEST")], default=1
            ),
        ),
    ]
