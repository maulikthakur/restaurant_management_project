from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = OrderItem        
        fields = ["name", "quantity", "price"]
        
class OrderHistorySerializer(serializers.ModelSerializer):    
    items = OrderItemSerializer(many=True, read_only=True)   
     
    class Meta:        
        model = Order        
        fields = ["id", "created_at", "total_amount", "status", "items"]