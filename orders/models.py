from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Assuming Menu items are stored in Product model

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('PREPARING', 'Preparing'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey("customers.Customer", on_delete=models.SET_NULL, null=True, blank=True)    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)    
    created_at = models.DateTimeField(auto_now_add=True)    
    #  Add the foreign key for status    
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)    
    
    def __str__(self):        
        return f"Order #{self.id} - {self.status.name if self.status else 'No Status'}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"

class OrderStatus(models.Model):    
    name = models.CharField(max_length=50, unique=True)    
    
    def __str__(self):        
        return self.name      
