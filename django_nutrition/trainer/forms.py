from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TrainerProfile, MealPlan, Food

class TrainerRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class TrainerUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class TrainerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ['image', 'company_name', 
            'phone_number', 'website', 'branding_image']

