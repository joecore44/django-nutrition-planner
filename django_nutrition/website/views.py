from django.shortcuts import render
from django.http import HttpResponse

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

def about(request):
    return HttpResponse('<h1>ABOUT</h1>')