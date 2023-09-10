# Generated by Django 4.1.10 on 2023-09-05 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0004_alter_companydocumentsmodel_companyid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementApplicationModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('interviewed', 'Interviewed'), ('placed', 'Placed')], default='applied', max_length=20)),
                ('appliedAt', models.DateTimeField(auto_now_add=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companymodel')),
                ('studentId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentApplicationDetail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
