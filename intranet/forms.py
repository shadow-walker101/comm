from django import forms
from .models import *

class Posting(forms.ModelForm):
    class Meta:
        model=Updates
        exclude=['user','time_stamp']



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['user', 'time_stamp']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder':'Write a comment...'})
        }