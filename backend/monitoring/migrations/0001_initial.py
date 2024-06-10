# Generated by Django 5.0.6 on 2024-06-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.FloatField()),
                ('site', models.CharField(max_length=255)),
                ('site_code', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('co_level', models.FloatField()),
                ('nox_level', models.FloatField()),
                ('no2_level', models.FloatField()),
                ('no_level', models.FloatField()),
                ('o3_level', models.FloatField()),
                ('so2_level', models.FloatField()),
                ('pm10_level', models.FloatField()),
                ('pm2_5_level', models.FloatField()),
                ('v10_level', models.FloatField()),
                ('v2_5_level', models.FloatField()),
                ('nv10_level', models.FloatField()),
                ('nv2_5_level', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.FloatField()),
                ('air_temperature', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('site_type', models.CharField(max_length=100)),
            ],
        ),
    ]