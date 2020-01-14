from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('notifications',views.notifications,name='notifications'),

    path('', views.updates, name='updates'),
    path('departments', views.departments, name='departments'),
    path('employees', views.employees, name='employees'),
]
