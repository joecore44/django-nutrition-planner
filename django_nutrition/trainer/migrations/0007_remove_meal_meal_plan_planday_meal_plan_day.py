# Generated by Django 4.1 on 2022-09-14 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0006_alter_food_image_alter_trainerprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='meal_plan',
        ),
        migrations.CreateModel(
            name='PlanDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.mealplan')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='plan_day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainer.planday'),
        ),
    ]
