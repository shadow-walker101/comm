from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from . models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME


def departments(request):
    return render(request, 'department.html')

def updates(request):
    return render(request, 'updates.html')

@login_required(login_url='accounts/login')
def employees(request):
    if request.user.user_type == 1 or request.user.user_type == 2:
        return render(request, 'employees.html')
    else:
        return render(request, 'employeeProfile.html')

@login_required(login_url='accounts/login')
def employeeProfile(request):
    return render(request, 'employeeProfile.html')

def notifications(request):
    return render(request, 'notifications.html')
