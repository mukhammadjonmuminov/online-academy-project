# Generated by Django 4.1.4 on 2023-01-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_course_modules'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'ordering': ['-id'], 'verbose_name': 'Speciality', 'verbose_name_plural': 'Specialitys'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='speciality',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
