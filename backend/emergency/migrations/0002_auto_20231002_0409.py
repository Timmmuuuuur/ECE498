# Generated by Django 3.2.20 on 2023-10-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='level',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='floorlayout',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
