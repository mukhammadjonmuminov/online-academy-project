# Generated by Django 4.1.4 on 2023-01-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_course_options_alter_speciality_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speciality',
            options={'ordering': ['id'], 'verbose_name': 'Speciality', 'verbose_name_plural': 'Specialitys'},
        ),
    ]
