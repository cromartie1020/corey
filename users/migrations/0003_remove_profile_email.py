# Generated by Django 3.2.6 on 2021-08-19 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
