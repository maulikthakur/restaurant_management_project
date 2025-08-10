from django.urls import path
from .views import *
from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):    
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('',home, name ='home'),
]