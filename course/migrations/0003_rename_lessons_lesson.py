# Generated by Django 4.0.4 on 2022-04-19 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_lessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]
