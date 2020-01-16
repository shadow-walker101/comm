from django.shortcuts import render , redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from . models import * 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from datetime import timedelta
import online_users.models



def login (request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('updates')
        

def departments(request):
    return render(request, 'department.html')
# @user_passes_test(lambda u: u.is_active and u.department==4,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def marketing(request):
    template='marketing.html'
    return render(request, template)

# @user_passes_test(lambda u: u.is_active and u.department==1,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def human_resource(request):
    template='human_resource.html'
    return render(request,template)


def updates(request):
    return render(request, 'updates.html')

# @user_passes_test(lambda u:u.is_active and u.department==3,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def finance(request):
    template='finance.html'
    return render(request,template)

# @user_passes_test(lambda u:u.is_active and u.department==2,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def inventory(request):
    template='inventory.html'
    return render(request,template)


# @user_passes_test(lambda u:u.is_active and u.department==5,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def information_technology(request):
    template='information_technology.html'
    return render(request,template)
  
def updates(request):
    template='updates.html'
    return render(request,template)


@login_required(login_url='accounts/login')
def employees(request):
    user_status = online_users.models.OnlineUserActivity.get_user_activities(timedelta(minutes=60))
    users = (user for user in user_status)
    context = {"online_users"}

    if request.user.user_type == 1 or request.user.user_type == 2:
        return render(request, 'employees.html')
    else:
        return render(request, 'employeeProfile.html')

def notifications(request):
    template='notifications.html'
    return render(request, template)
  
@login_required(login_url='accounts/login')
def employeeProfile(request):
    return render(request, 'employeeProfile.html')


def postUpdate(request):
    
    return render(request, 'postUpdate.html')

def searchResults(request):
    
    return render(request, 'searchResults.html')