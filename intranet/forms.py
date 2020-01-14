from django import forms
from .models import *
from django.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm)
username=forms.CharField(max_length=30)
email=forms.EmailField(max_length=200)

class meta:
    model=User
    fields=('username','email','user_type','department','employee_id')