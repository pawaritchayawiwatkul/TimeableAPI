# Generated by Django 4.2.13 on 2024-06-17 03:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_school_registered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='start',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
        migrations.AddField(
            model_name='school',
            name='stop',
            field=models.TimeField(default=datetime.time(15, 0)),
        ),
    ]
