# Generated by Django 4.2.13 on 2024-07-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_courseregistration_exp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseregistration',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='courseregistration',
            name='finished',
        ),
        migrations.AddField(
            model_name='courseregistration',
            name='status',
            field=models.CharField(choices=[('PEN', 'Pending'), ('COM', 'Completed'), ('EXP', 'Expired')], default='PEN', max_length=3),
        ),
    ]
