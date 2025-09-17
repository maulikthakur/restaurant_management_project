import secrets
import string
from .models import Coupon  

# assuming youll have a Coupon model later
def generate_coupon_code(length=10):    
    """
    Generate a unique alphanumeric coupon code.    
    Default length = 10 characters.    
    Ensures uniqueness by checking existing Coupon records.    
    """    
    
    alphabet = string.ascii_uppercase + string.digits    
    
    while True:        
        # Generate random code        
        code = ''.join(secrets.choice(alphabet)  for _ in range(length))                
        
        # Check uniqueness against database        
        if not Coupon.objects.filter(code=code).exists():            
            return code