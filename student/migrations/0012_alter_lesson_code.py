# Generated by Django 4.2.13 on 2024-06-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_lesson_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='code',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
