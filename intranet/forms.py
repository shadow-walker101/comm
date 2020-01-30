from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from . email import send_credentials


class Posting(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['user', 'time_stamp']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['user', 'time_stamp', 'status']
        widgets = {
            'update': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:

        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Write a comment...'})
        }


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'user_type', 'department', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        credential = self.cleaned_data["password1"]
        email = user.email
        username = user.username
        send_credentials(credential,username,email)
        
        return user
