# Generated by Django 4.1.10 on 2023-08-28 17:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculty', '0003_alter_facultypersonalmodel_facultyid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacultyPersonalModel',
            new_name='FacultyModel',
        ),
    ]
