from django.urls import path
from .views import ProductListAPIView

urlpatterns = [
    path('api/menu/', ProductListAPIView.as_view(), name='menu-api'),
]
