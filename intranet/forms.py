from django import forms
from .models import *



class Posting(forms.ModelForm):
    class Meta:
        model=Updates
        exclude=['user','time_stamp']


