# Generated by Django 5.0.6 on 2024-06-08 09:05

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
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('light_intensity', models.BooleanField()),
                ('motion_presence', models.BooleanField()),
                ('smoke_detected', models.FloatField()),
                ('gas_leak_detected', models.FloatField()),
            ],
        ),
    ]
