# Generated by Django 4.1.4 on 2023-01-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_teacher_slug_alter_course_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(blank=True, to='app.module'),
        ),
    ]
