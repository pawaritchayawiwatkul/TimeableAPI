# Generated by Django 4.2.13 on 2024-06-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_rename_favorite_courseregistration_student_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseregistration',
            name='teacher_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
