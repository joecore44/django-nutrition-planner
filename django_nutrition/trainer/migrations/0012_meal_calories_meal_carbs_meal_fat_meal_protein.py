# Generated by Django 4.1 on 2022-09-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0011_alter_planday_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='calories',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='carbs',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='protein',
            field=models.FloatField(null=True),
        ),
    ]
