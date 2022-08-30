from django.db import models
from django.contrib.auth.models import User

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
        upload_to='trainer_media/profile')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    website = models.CharField(max_length=24)
    branding_image = models.ImageField(default='default.jpg',
        upload_to='trainer_media')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

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

    def __str__(self):
            return self.title

class Meal(models.Model):
    # TODO figure out what to do about 
    # tying the meal to the plan and user but
    # don't make it manditory
    meal_plan = models.ForeignKey(MealPlan, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=36)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',
        upload_to='trainer_media/meals')

    def __str__(self):
            return self.title

class Food(models.Model):
    # TODO figure out what to do about 
    # tying the food to the meal and user but
    # don't make it manditory
    meal = models.ForeignKey(Meal, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=36)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',
        upload_to='trainer_media/meals/food')
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
            return self.title
