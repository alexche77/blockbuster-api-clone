# Generated by Django 3.1.8 on 2021-04-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0019_auto_20210414_1939"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movement",
            name="comments",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
