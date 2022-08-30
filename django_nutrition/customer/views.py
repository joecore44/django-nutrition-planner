from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'customer/index.html', context)