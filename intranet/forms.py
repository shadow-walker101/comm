from django import forms
from .models import *
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['user', 'time_stamp']
