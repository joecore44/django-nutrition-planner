from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webiste-home'),
    path('about/', views.about, name='webiste-about'),
    # Sends request from the main app's URL request to this one then to the views.py file
]