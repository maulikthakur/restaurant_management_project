from django.contrib import admin
from .models import UserProfile
from .models import RestaurantInfo

admin.site.register(RestaurantInfo)

admin.site.register(UserProfile)

