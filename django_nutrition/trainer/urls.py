from django.urls import path
from .views import MealPlanListView, MealPlanDetailView
from . import views

urlpatterns = [
    path('', views.home, name='trainer-home'),
    path('meal-plans', MealPlanListView.as_view(), name='meal-plans'),
    path('meal-plan/<int:pk>/', MealPlanDetailView.as_view(), name='meal-plan')
]