from django.urls import path
from .views import ProductListAPIView
from .views import HardcodedMenuAPIView
from django.urls import path, include

urlpatterns = [
    path('api/menu/', ProductListAPIView.as_view(), name='menu-api'),
    path('api/menu/', HardcodedMenuAPIView.as_view(), name='hardcoded-menu-api'),
    path('products/', include('products.urls')),
    path('menu/', menu_view, name='maenu-page')
    
]


