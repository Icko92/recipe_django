# Generated by Django 3.1.6 on 2021-02-28 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_picture',
        ),
    ]
