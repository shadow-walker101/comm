
from django.shortcuts import render
from django.contrib.auth import login,authenticate
from .models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME

@user_passes_test(lambda u: u.is_active and u.department==4,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def marketing(request):
    template='marketing.html'
    return render(request, template)

@user_passes_test(lambda u: u.is_active and u.department==1,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def human_resource(request):
    template='human_resource.html'
    return render(request,template)

@user_passes_test(lambda u:u.is_active and u.department==3,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def finance(request):
    template='finance.html'
    return render(request,template)

@user_passes_test(lambda u:u.is_active and u.department==2,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def inventory(request):
    template='inventory.html'
    return render(request,template)

@user_passes_test(lambda u:u.is_active and u.department==5,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def information_technology(request):
    template='information_technology.html'
    return render(request,template)
    
    



def departments(request):
    return render(request, 'human_resource.html')


def updates(request):

    return render(request, 'updates.html')

@login_required(login_url='accounts/login')
def employees(request):

    template="employees.html"
    return render(request,template)
    
    return render(request, 'employees.html')

def notifications(request):
    return render(request, 'notifications.html')

def login(request):
    return render(request, 'login.html')
    if request.user.user_type == 1 or request.user.user_type == 2:
        return render(request, 'employees.html')
    else:
        return render(request, 'employeeProfile.html')

@login_required(login_url='accounts/login')
def employeeProfile(request):
    return render(request, 'employeeProfile.html')


