# Generated by Django 4.1.4 on 2022-12-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_course_modules_alter_lesson_part_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='members',
            field=models.PositiveIntegerField(auto_created=True, default=0),
        ),
    ]
