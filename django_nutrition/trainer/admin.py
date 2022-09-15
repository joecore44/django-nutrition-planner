from django.contrib import admin
from . models import BillingPlan, TrainerProfile, MealPlan, PlanDay, Meal, Food

admin.site.register(TrainerProfile)
admin.site.register(MealPlan)
admin.site.register(PlanDay)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(BillingPlan)
