# Generated by Django 4.2.13 on 2024-07-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_remove_courseregistration_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('PEN', 'Pending'), ('CON', 'Confirmed'), ('COM', 'Completed'), ('CAN', 'Canceled'), ('MIS', 'Missed')], default='PEN', max_length=3),
        ),
    ]
