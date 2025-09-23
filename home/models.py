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

class MenuItem(models.Model):    
    name = models.CharField(max_length=150)    
    description = models.TextField(blank=True, null=True)    
    price = models.DecimalField(max_digits=8, decimal_places=2)    
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name="items")    
    
    def __str__(self):        
        return self.name        