# Generated by Django 5.0.6 on 2024-06-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_sensordata_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='co_level',
            field=models.FloatField(default=0.0),
        ),
    ]
