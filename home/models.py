from django.db import models

class Contact(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        submitted_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.name} - {self.email}"

class RestaurantInfo(models.Model):
        name = models.CharField(max_length=100)
        address = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return self.name

class MenuCategory(models.Model):    
    name = models.CharField(max_length=100, unique=True)    
    
    def __str__(self):        
        return self.name            