# Generated by Django 3.2.20 on 2023-07-14 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(max_length=7)),
                ('latitude', models.FloatField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('kind', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(max_length=25)),
                ('building', models.CharField(max_length=25)),
                ('room', models.CharField(max_length=7)),
                ('floor', models.IntegerField(default=0)),
                ('coordinate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.coordinate')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_number', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=20)),
                ('emergency', models.BooleanField()),
                ('crime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.crime')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.location')),
            ],
        ),
    ]
