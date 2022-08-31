from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import TrainerRegisterForm

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
            return redirect('website-home')
    else:
        form = TrainerRegisterForm()
    return render(request, 'trainer/register.html', {'form': form})

