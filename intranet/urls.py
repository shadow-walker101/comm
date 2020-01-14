from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('', views.departments, name='departments'),
    path('updates', views.updates, name='updates'),
    path('employees', views.employees, name='employees')
]
