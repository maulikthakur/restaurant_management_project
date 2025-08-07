
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import Restaurant


def home(request):    
    restaurant = Restaurant.objects.first()    
    return render(request, 'account/homes.html', {'restaurant': restaurant})




def contact_view(request):    
    if request.method == 'POST':        
        form = ContactForm(request.POST)        
        if form.is_valid():            
            contact = form.save()           
            
            # Send email            
            subject = 'New Contact Form Submission'            
            message = f"Name: {contact.name}\nEmail: {contact.email}"           
            recipient = 'restaurant@example.com'  # Replace with actual restaurant email   

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient]) 

            return redirect('contact_success')    
    else:        
        form = ContactForm()    
    return render(request, 'account/contact.html', {'form': form})"



class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    
    # Additional order information
    order_notes = models.TextField(blank=True, null=True, help_text="Special instructions")
    delivery_address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username} - ${self.total_amount}"
    
    def calculate_total(self):
        """Calculate total

    


