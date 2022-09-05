from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TrainerRegisterForm, TrainerUpdateForm, TrainerProfileUpdateForm
from .models import MealPlan

plans = [
    {
        'title': 'Customer Plan 1',
        'body': 'Body 1',
        'price': '$29.99'
    }, {
        'title': 'Customer Plan 2',
        'body': 'Body 2',
        'price': '$39.99'
    }, 
    {
        'title': 'Customer Plan 3',
        'body': 'Body 3',
        'price': '$49.99'
    }
]
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

class MealPlanDetailView(DetailView):
    model = MealPlan

class MealPlanCreateView(CreateView):
    model = MealPlan
    fields = ['image', 'title', 'description', 'free_plan',
     'diet_type', 'meal_type']

    def form_valid(self, form):
        form.instance.trainer = self.request.user.trainerprofile
        return super().form_valid(form)