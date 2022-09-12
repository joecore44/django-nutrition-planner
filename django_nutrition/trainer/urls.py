from django.urls import path
from .views import MealPlanListView, MealPlanDetailView, MealPlanCreateView, MealListView, MealDetailView, MealCreateView
from .views import FoodListView, FoodDetailView, FoodCreateView
from . import views

urlpatterns = [
    path('', views.home, name='trainer-home'),
    # Plan URLs
    path('meal-plans', MealPlanListView.as_view(), name='meal-plans'),
    path('meal-plan/<int:pk>/', MealPlanDetailView.as_view(), name='meal-plan'),
    path('meal-plan/new/', MealPlanCreateView.as_view(), name='meal-plan-create'),
    # Meals URLs
    path('meals', MealListView.as_view(), name='meals'),
    path('meal/<int:pk>/', MealDetailView.as_view(), name='meal'),
    path('meal/new/', MealCreateView.as_view(), name='meal-create'),
    # Food URLs
    #path('foods', FoodListView.as_view(), name='foods'),
    #path('food/<int:pk>/',FoodDetailView.as_view(), name='food'),
    path('food/new/', FoodCreateView.as_view(), name='food-create'),
 
    path('foods/', views.get_foods, name = "get-foods"),
    #path('foods/<int:id>/',views.food_detail, name = "food-detail")

]