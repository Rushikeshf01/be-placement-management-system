# Generated by Django 4.1.10 on 2023-08-15 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyPersonalModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('profilePic', models.FileField(upload_to='faculty_profile_pic/')),
                ('alternateMobile', models.CharField(max_length=150)),
                ('alternateEmail', models.EmailField(max_length=150, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('facultyId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
