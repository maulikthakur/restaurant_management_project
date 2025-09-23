from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path("order-history/", OrderHistoryView.as_view(), name="order-history"),  
]