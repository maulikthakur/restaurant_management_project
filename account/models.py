from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):    
    name = models.CharField(max_length=255)    
    address = models.TextField()    city = models.CharField(max_length=100)    
    state = models.CharField(max_length=100)    zip_code = models.CharField(max_length=10)    
    
    
    # Add opening_hours as a JSON field (requires PostgreSQL or Django 3.1+)    
    opening_hours = {    
        "Monday": "9 AM  10 PM",    
        "Tuesday": "9 AM  10 PM",    
        "Wednesday": "9 AM  10 PM",    
        "Thursday": "9 AM  10 PM",    
        "Friday": "9 AM  11 PM",    
        "Saturday": "10 AM  11 PM",    
        "Sunday": "10 AM  9 PM"
        }   
    
    
    def __str__(self):        
        return self.name