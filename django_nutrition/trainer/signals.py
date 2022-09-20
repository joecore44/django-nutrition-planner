from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PlanDay, TrainerProfile, Meal, Food

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        TrainerProfile.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.trainer.save()
'''

@receiver(post_save, sender=Food)
def create_food(sender, instance, created, **kwargs):
    if created:
        meal = Meal.objects.filter(pk=instance.meal.id).first()
        meal.protein += instance.protein
        meal.carbs += instance.carbs
        meal.fat += instance.fat
        meal.calories += instance.calories
        meal.save()

@receiver(post_delete, sender=Food)
def delete_food(sender, instance, *args, **kwargs):
    meal = Meal.objects.filter(pk=instance.meal.id).first()
    meal.protein -= instance.protein
    meal.carbs -= instance.carbs
    meal.fat -= instance.fat
    meal.calories -= instance.calories
    meal.save()
 

@receiver(post_save, sender=Food)
def save_food(sender, instance, **kwargs):
    meal = Meal.objects.filter(pk=instance.meal.id).first()
    foods = Food.objects.filter(meal=instance.meal.id).all()
    protein = 0
    fat = 0
    carbs = 0
    calories = 0
    for food in foods:
        protein += food.protein
        fat += food.fat
        carbs += food.carbs
        calories += food.calories
    meal.protein = protein
    meal.fat = fat
    meal.carbs = carbs
    meal.calories = calories
    meal.save()
    
        

        