from django.urls import path
from .views import MealPlanListView, MealPlanDetailView, MealPlanCreateView
from . import views

urlpatterns = [
    path('', views.home, name='trainer-home'),
    path('meal-plans', MealPlanListView.as_view(), name='meal-plans'),
    path('meal-plan/<int:pk>/', MealPlanDetailView.as_view(), name='meal-plan'),
    path('meal-plan/new/', MealPlanCreateView.as_view(), name='meal-create')

]