# Generated by Django 4.2.2 on 2023-07-07 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0002_meow"),
    ]

    operations = [
        migrations.CreateModel(
            name="coordinate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Longitude", models.FloatField(max_length=7)),
                ("Latitude", models.FloatField(max_length=7)),
                ("Floor", models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="crime",
            fields=[
                (
                    "Type",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("Description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Campus", models.CharField(max_length=25)),
                ("Building", models.CharField(max_length=25)),
                ("Room", models.CharField(max_length=7)),
                (
                    "Coordinate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="playground.coordinate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="report",
            fields=[
                (
                    "Report_number",
                    models.IntegerField(
                        max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("Date", models.DateTimeField(auto_now=True)),
                ("Status", models.CharField(max_length=20)),
                ("Emergency", models.BooleanField()),
                (
                    "Crime",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="playground.crime",
                    ),
                ),
                (
                    "Location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="playground.location",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="meow",),
        migrations.DeleteModel(name="SearchLog",),
    ]
