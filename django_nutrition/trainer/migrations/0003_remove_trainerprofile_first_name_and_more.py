# Generated by Django 4.1 on 2022-08-31 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_billingplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainerprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='trainerprofile',
            name='last_name',
        ),
    ]
