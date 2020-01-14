from django.shortcuts import render
from django.contrib.auth import login,authenticate
from .models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME




# Create your views here.
def departments(request):
    return render(request, 'department.html')

def human_resource(request):
    return render(request,'human_resource.html')


def updates(request):

    return render(request, 'updates.html')



def employees(request):
    template="employees.html"
    return render(request,template)
    
    return render(request, 'employees.html')

def notifications(request):
    return render(request, 'notifications.html')
