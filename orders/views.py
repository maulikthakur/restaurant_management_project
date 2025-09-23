from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderHistorySerializer

class OrderHistoryView(APIView):    
    permission_classes = [IsAuthenticated]    
    
    def get(self, request):        
        orders = Order.objects.filter(user=request.user).order_by("-created_at")        
        serializer = OrderHistorySerializer(orders, many=True)        
        return Response(serializer.data)