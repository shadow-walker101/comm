from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.updates, name='updates'),
    path('departments', views.departments, name='departments'),
    path('employees', views.employees, name='employees'),

    path('inventory', views.inventory, name='inventory'),
    path('finance', views.finance, name='finance'),
    path('marketing', views.marketing, name='marketing'),
    path('information', views.information, name='information'),

    path('employeeProfile', views.employeeProfile, name='employeeProfile')
]

