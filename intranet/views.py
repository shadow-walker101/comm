from django.shortcuts import render , redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from . models import * 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME


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



def updates(request):
    return render(request, 'updates.html')


@user_passes_test(lambda u:u.is_active , login_url='/accounts/login')
def employees(request):
    return render(request, 'employees.html')

def notifications(request):
    return render(request, 'notifications.html')
