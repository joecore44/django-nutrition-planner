from tkinter import EW
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse



class TrainerProfile(models.Model):
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
        upload_to='profile')
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    website = models.CharField(max_length=24)
    branding_image = models.ImageField(default='default.jpg',
        upload_to='trainer_media')

    def save(self):
        super.save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username}'

class MealPlan(models.Model):
    trainer = models.ForeignKey(TrainerProfile, 
        on_delete=models.CASCADE)
    title = models.CharField(max_length=36)
    free_plan = models.BooleanField(default=True)
    description = models.TextField()
    diet_type = models.CharField(max_length=20)
    meal_type = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg',
        upload_to='trainer_media/meals')

    def get_absolute_url(self):
        return reverse('meal-plan', kwargs={'pk': self.pk})

    def __str__(self):
            return self.title

class PlanDay(models.Model):
    meal_plan = models.ForeignKey(MealPlan,
    on_delete=models.CASCADE)
    day_number = models.IntegerField()
    date = models.DateField(null=True)
    def __str__(self):
        
        day = 'Meal Plan ' + str(self.meal_plan) + ' Day ' + str(self.day_number)
        return day

class Meal(models.Model):
    # TODO figure out what to do about 
    # tying the meal to the plan and user but
    # don't make it manditory
    # TODO add time to the Meal model (EX: Breakfast, Post Workout)
    #meal_plan = models.ForeignKey(MealPlan, null=True, on_delete=models.SET_NULL)
    plan_day = models.ForeignKey(PlanDay, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=36)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',
        upload_to='trainer_media/meals')
    protein = models.FloatField(null=True, default=0)
    carbs = models.FloatField(null=True, default=0)
    fat = models.FloatField(null=True, default=0)
    calories = models.FloatField(null=True, default=0)

    def get_absolute_url(self):
        return reverse('meal', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Food(models.Model):
    # TODO figure out what to do about 
    # tying the food to the meal and user but
    # don't make it manditory
    meal = models.ForeignKey(Meal, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=36)
    description = models.TextField()
    image = models.CharField(max_length=250)
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    calories = models.FloatField()

    def get_absolute_url(self):
        return reverse('food', kwargs={'pk': self.pk})

    def __str__(self):
            return self.title

class BillingPlan(models.Model):
    trainer = models.ForeignKey(TrainerProfile, 
        on_delete=models.CASCADE)
    title = models.CharField(max_length=36)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    includes = models.TextField()
    how_it_works = models.TextField()
    image = models.ImageField(default='default.jpg',
        upload_to='trainer_media/billing')

    def __str__(self):
            return self.title
