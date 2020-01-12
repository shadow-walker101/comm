from django.shortcuts import render

# Create your views here.


def updates(request):
    return render(request, 'updates.html')
