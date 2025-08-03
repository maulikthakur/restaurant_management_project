from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.



def some_view(request):
    user = User.objects.get(username='example_user')
    profile = user.profile
    phone = profile.phone_number
    

