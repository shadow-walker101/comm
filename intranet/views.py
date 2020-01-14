from django.shortcuts import render

# Create your views here.


def updates(request):
    return render(request, 'updates.html')

def departments(request):
    return render (request, 'departments.html')

def employees(request):
    return render(request, 'employees.html')

def notifications(request):
    return render(request, 'notifications.html')

