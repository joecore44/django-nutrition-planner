# Generated by Django 4.1 on 2022-09-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0007_remove_meal_meal_plan_planday_meal_plan_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planday',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
