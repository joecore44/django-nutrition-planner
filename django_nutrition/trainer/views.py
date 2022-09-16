from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TrainerRegisterForm, TrainerUpdateForm, TrainerProfileUpdateForm
from .models import MealPlan, PlanDay, Meal, Food
from django.forms import modelformset_factory
import requests


def home(request):
    context = {
        'plans': plans,
        'title': 'FUCK YEAH'
    }
    return render(request, 'trainer/index.html', context)

def register(request):
    if request.method == 'POST':
        form = TrainerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}!')
            return redirect('login')
    else:
        form = TrainerRegisterForm()
    return render(request, 'trainer/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = TrainerUpdateForm(request.POST,
                                    instance=request.user)
        p_form  = TrainerProfileUpdateForm(request.POST,
                                    instance=request.user.trainerprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        u_form = TrainerUpdateForm(instance=request.user)
        p_form  = TrainerProfileUpdateForm(instance=request.user.trainerprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'trainer/profile.html', context)

class MealPlanListView(ListView):
    model = MealPlan
    context = {
        'plans': MealPlan.objects.all()
    }
    context_object_name = 'plans'

    def get_queryset(self):
        return super(MealPlanListView, self).get_queryset().filter(trainer=self.request.user.trainerprofile)

class MealPlanDetailView(DetailView):
    model = MealPlan

    def get_context_data(self, *args, **kwargs):
        context = super(MealPlanDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context['days'] = PlanDay.objects.select_related().filter(meal_plan=instance)
        return context

    '''
    def get_context_data(self, *args, **kwargs):
        context = super(MealPlanDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context['meals'] = Meal.objects.select_related().filter(meal_plan=instance)
        return context
    '''
class DayDetailView(DetailView):
    model = PlanDay

    def get_context_data(self, *args, **kwargs):
        context = super(DayDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context['meals'] = Meal.objects.select_related().filter(plan_day=instance)
        return context


class MealPlanCreateView(CreateView):
    model = MealPlan
    fields = ['image', 'title', 'description', 'free_plan',
     'diet_type', 'meal_type']

    def form_valid(self, form):
        form.instance.trainer = self.request.user.trainerprofile
        return super().form_valid(form)

class MealListView(ListView):
    model = Meal
    context = {
        'meals': Meal.objects.all()
    }
    context_object_name = 'meals'

class MealDetailView(DetailView):
    model = Meal

    def get_context_data(self, *args, **kwargs):
        context = super(MealDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context['foods'] = Food.objects.select_related().filter(meal=instance)
        return context



@login_required
def CreateMeal(request, plan_day):
    MealFormSet = modelformset_factory(Meal, fields=(
        'plan_day', 'image', 'title', 'description'
    ))
    if request.method == 'POST':
        form = MealFormSet(request.POST)
        instances = form.save()

        return redirect('day-detail', pk=plan_day)
    form = MealFormSet(queryset=Meal.objects.none(), initial=[{'plan_day': plan_day}])
    return render(request, 'trainer/meal_form.html', {'form': form})


class MealCreateView(CreateView):
    model = Meal
    fields = ['meal_plan', 'image', 'title', 'description']

    def form_valid(self, form):
        form.instance.trainer = self.request.user.trainerprofile
        return super().form_valid(form)

@login_required
def CreateFood(request, meal):
    FoodFormSet = modelformset_factory(Food, fields=(
        'meal', 'image', 'title', 'description', 'protein', 'carbs', 'fat', 'calories'
    ))
    if request.method == 'POST':
        form = FoodFormSet(request.POST)
        instances = form.save()

        return redirect('meal', pk=meal)
    form = FoodFormSet(queryset=Food.objects.none(), initial=[{'meal': meal}])
    return render(request, 'trainer/meal_form.html', {'form': form})


class FoodListView(ListView):
    model = Food
    context = {
        'foods': Food.objects.all()
    }
    context_object_name = 'foods'

class FoodDetailView(DetailView):
    model = Food

class FoodCreateView(CreateView):
 
    model = Food
    fields = ['meal', 'image', 'title', 'description', 'protein', 'carbs', 'fat', 'calories']
    #success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

    def form_valid(self, form):
        form.instance.meal = 'Breakfast'
        form.instance.trainer = self.request.user.trainerprofile
        return super().form_valid(form)

def get_foods(request):
        if 'name' in request.GET:
            name = request.GET['name']
            url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

            querystring = {"ingr":name}
            headers = {}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = response.json()
            foods = data['hints']
            food_list = []
            for food in foods:
                if 'image' in food['food']:
                    image = food['food']['image']
                else:
                    image = 'https://www.edamam.com/food-img/093/093749f4c93e448119fc81976d2c3067.jpg'
                items = {
                'food_id' : food['food']['foodId'],   
                'kcal' : int(food['food']['nutrients']['ENERC_KCAL']),
                'protein': int(food['food']['nutrients']['PROCNT']),
                'carbs': int(food['food']['nutrients']['CHOCDF']),
                'fat': int(food['food']['nutrients']['FAT']),
                'category': food['food']['category'],
                'title': food['food']['label'],
                'image': image
                }
                food_list.append(items)
            

            return render(request, 'trainer/food.html', {'food_data': food_list})
        else:
            return render(request, 'trainer/food.html')
 


    
