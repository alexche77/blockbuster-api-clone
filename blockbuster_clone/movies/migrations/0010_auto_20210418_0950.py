# Generated by Django 3.1.8 on 2021-04-18 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_remove_movie_movements'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-updated_at']},
        ),
    ]