# Generated by Django 3.2.12 on 2023-02-15 10:21

import CustomUser.managers
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', CustomUser.managers.UserManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
