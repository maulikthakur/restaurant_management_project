from rest_framework import serializersfrom 
.models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):    
    class Meta:        
        model = MenuCategory        
        fields = ['id', 'name']  # include id so frontend can identify categories