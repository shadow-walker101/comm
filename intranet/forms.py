from django import forms
from .models import *



class Post(forms.ModelForm):
    class Meta:
        model=Updates
        exclude=['user','time_stamp']


