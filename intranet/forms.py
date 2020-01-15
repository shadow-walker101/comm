from django import forms
from .models import *
from django.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm)
username=forms.CharField(max_length=30)
email=forms.EmailField(max_length=200)

class meta:
    model=User
    fields=('username','email','user_type','departments','employee_id')

class LoginForm()

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['user', 'time_stamp']
