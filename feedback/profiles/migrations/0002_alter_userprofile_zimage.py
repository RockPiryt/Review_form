# Generated by Django 4.2.5 on 2023-09-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zimage',
            field=models.ImageField(upload_to='user_images'),
        ),
    ]
