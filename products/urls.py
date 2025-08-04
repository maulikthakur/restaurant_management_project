from django.urls import path
from .views import ProductListAPIView
from .views import HardcodedMenuAPIView

urlpatterns = [
    path('api/menu/', ProductListAPIView.as_view(), name='menu-api'),
    path('api/menu/', HardcodedMenuAPIView.as_view(), name='hardcoded-menu-api'),
    
]

