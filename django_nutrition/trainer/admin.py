from django.contrib import admin
from . models import TrainerProfile, MealPlan, Meal, Food

admin.site.register(TrainerProfile)
admin.site.register(MealPlan)
admin.site.register(Meal)
admin.site.register(Food)
