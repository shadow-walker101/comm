from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [

    path('', views.updates, name='updates'),
    path('notifications', views.notifications, name='notifications'),
    path('employees', views.employees, name='employees'),
    path('login', views.login, name='login'),
    path('inventory', views.inventory, name='inventory'),
    path('finance', views.finance, name='finance'),
    path('marketing', views.marketing, name='marketing'),
    path('information', views.information_technology, name='information'),
    path('employeeProfile', views.employeeProfile, name='employeeProfile'),
    path('human_resource',views.human_resource,name='human_resource')

]

