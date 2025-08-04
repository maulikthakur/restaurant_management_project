from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HardcodedMenuAPIView(APIView):
    def get(self, request):
        menu = [
            {
                "name": "Margherita Pizza",
                "description": "Classic pizza with tomato sauce and mozzarella cheese",
                "price": 249.00
            },
            {
                "name": "Paneer Tikka",
                "description": "Grilled paneer cubes with spicy marinade",
                "price": 199.00
            },
            {
                "name": "Masala Dosa",
                "description": "Crispy dosa filled with spiced mashed potatoes",
                "price": 129.00
            }
        ]
        return Response(menu, status=status.HTTP_200_OK)


