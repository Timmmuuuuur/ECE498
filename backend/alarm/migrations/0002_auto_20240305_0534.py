# Generated by Django 3.2.20 on 2024-03-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='active',
        ),
        migrations.AddField(
            model_name='alarm',
            name='alarm',
            field=models.BooleanField(default=False),
        ),
    ]