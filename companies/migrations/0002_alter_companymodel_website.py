# Generated by Django 4.1.10 on 2023-08-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='website',
            field=models.CharField(max_length=150),
        ),
    ]