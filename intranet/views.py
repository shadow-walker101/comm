from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate
from . models import * 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from datetime import timedelta
import online_users.models
from .forms import *




def login (request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('updates')


@login_required(login_url='accounts/login')      
def updates(request):
    updates = Updates.objects.filter(department=1).all()[::-1]
    users = User.objects.order_by('-last_login')
    comments = Comments.objects.all()
    commentForm = CommentForm()
    
    return render(request, 'updates.html', locals())

def marketing(request):
    template='marketing.html'
    updates = Updates.objects.filter(department=5).all()
    return render(request, template,{'updates':updates})

# @user_passes_test(lambda u: u.is_active and u.department==1,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')

def human_resource(request):
    template='human_resource.html'
    updates = Updates.objects.filter(department=2).all()
    return render(request,template, {'updates':updates})


# @user_passes_test(lambda u:u.is_active and u.department==3,redirect_field_name=REDIRECT_FIELD_NAME,login_url='account/login')
def finance(request):
    template='finance.html'
    updates = Updates.objects.filter(department=6).all()
    return render(request,template,{'update':updates})

# @user_passes_test(lambda u:u.is_active and u.department==2,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')
def inventory(request):
    updates = Updates.objects.filter(department=4).all()
    users = User.objects.order_by('-last_login')
    comments = Comments.objects.all()
    commentForm = CommentForm()
    return render(request, 'inventory.html', locals())


# @user_passes_test(lambda u:u.is_active and u.department==5,redirect_field_name=REDIRECT_FIELD_NAME,login_url='accounts/login')
def information_technology(request):
    template='information_technology.html'
    updates = Updates.objects.filter(department=3).all()
    return render(request,template,{'update':updates})

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
    

def employeeProfile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    return render(request, 'employeeProfile.html', {'profile':profile})


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
  
def searchResults(request):
    return render(request, 'searchResults.html')


#comments
@login_required(login_url='/accounts/login')
def comments(request, update_id):
    commentForm = CommentForm()
    update = get_object_or_404(Updates,pk=update_id)
        
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():            
            form = commentForm.save(commit=False)
            form.user=request.user
            form.update=get_object_or_404(Updates,pk=update_id)
            form.save()
        return redirect ('updates')
    return render (request, 'updates.html', locals())