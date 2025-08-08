from django.urls import path
from .views import ProductListAPIView
from .views import HardcodedMenuAPIView
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/menu/', ProductListAPIView.as_view(), name='menu-api'),
    path('api/menu/', HardcodedMenuAPIView.as_view(), name='hardcoded-menu-api'),
    path('products/', include('products.urls')),
    path('menu/', views.menu_view, name='menu')
    
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


