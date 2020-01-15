from django import forms
from .models import *



class Post(forms.ModelForm):
    class Meta:
        model=Updates


class UserRegistrationForm(UserCreationForm)
username=forms.CharField(max_length=30)
email=forms.EmailField(max_length=200)

class meta:
    model=User
    fields=('username','email','user_type','departments','employee_id')

class LoginForm()
