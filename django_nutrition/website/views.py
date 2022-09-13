from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


plans = [
    {
        'title': 'Plan 1',
        'body': 'Body 1',
        'price': '$29.99'
    }, {
        'title': 'Plan 2',
        'body': 'Body 2',
        'price': '$39.99'
    }, 
    {
        'title': 'Plan 3',
        'body': 'Body 3',
        'price': '$49.99'
    }
]
def home(request):
    context = {
        'plans': plans
    }
    return render(request, 'website/index.html', context)

@login_required
def profile(request):
    return render(request, 'website/profile.html')