# Generated by Django 3.2.20 on 2023-10-02 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0002_auto_20231002_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='layout',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='layout', to='emergency.floorlayout'),
        ),
    ]
