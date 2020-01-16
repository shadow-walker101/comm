from django.shortcuts import render , redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from . models import * 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from .forms import *



def login (request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('updates')


        
def updates(request):
    updates = Updates.objects.filter(department=1).all()
    return render(request, 'updates.html' ,{'updates':updates})

def marketing(request):
    template='marketing.html'
    updates = Updates.objects.filter(department=5).all()
    return render(request, template,{'updates':updates})

# @user_passes_test(lambda u: u.is_active and u.department==1,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')

def human_resource(request):
    template='human_resource.html'
    updates = Updates.objects.filter(department=2).all()
    return render(request,template, {'updates':updates})

# @user_passes_test(lambda u:u.is_active and u.department==3,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')
def finance(request):
    template='finance.html'
    updates = Updates.objects.filter(department=6).all()
    return render(request,template,{'update':updates})

# @user_passes_test(lambda u:u.is_active and u.department==2,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')
def inventory(request):
    template='inventory.html'
    updates = Updates.objects.filter(department=4).all()
    return render(request,template,{'update':updates})


# @user_passes_test(lambda u:u.is_active and u.department==5,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')
def information_technology(request):
    template='information_technology.html'
    updates = Updates.objects.filter(department=3).all()
    return render(request,template,{'update':updates})

@login_required(login_url='accounts/login')
def employees(request):
    template='employees.html'
    return render(request, template)


def notifications(request):
    template='notifications.html'
    return render(request, template)
    

def employeeProfile(request):
    return render(request, 'employeeProfile.html')

@login_required(login_url='accounts/login')
def postUpdate(request):
    current_user =  request.user
    if current_user.user_type == 1 or current_user.user_type==2:
        if request.method == 'POST':
            form = PostUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = current_user
                post.save()
            return redirect('updates')
        else:
            form = PostUpdateForm()
            return render(request, 'postUpdate.html', {"form":form})
    return redirect('updates')