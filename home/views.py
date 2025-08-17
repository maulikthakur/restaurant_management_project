from django.shortcuts import render

# Create your views here:
from django.conf import settings

def home(request):
    from .forms import ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    restaurant = RestaurantInfo.objects.first()    

    context = {
        'form': form,
        'restaurant_name': settings.RESTAURANT_NAME,
        'phone_number':settings.RESTAURANT_PHONE
        'restaurant_address': restaurant.address if restaurant and restaurant.address else 'Babariya Near Babariya Lake Road, Seoni, Madhya Pradesh (480661)'   
    }

    return render(request,'homes.html', context)

def reservations(request):    
    try:        
        # For now, just a placeholder (later this could be a DB query)        
        message = "Reservations feature coming soon!"                
        # Example of future DB logic (wrapped in try)        
        # reservations = Reservation.objects.all()        
        # return render(request, "reservations/list.html", {"reservations": reservations})        
        
        return render(request, "reservations/reservations.html", {"message": message})    

    except DatabaseError:        
        # Handle DB-related issues gracefully        
        error_message = "Sorry, were having trouble fetching reservations right now. Please try again later."       
        return render(request, "reservations/reservations.html", {"error": error_message})    
        
    except Exception as e:        
        # Catch-all for unexpected errors        
        error_message = f"An unexpected error occurred: {str(e)}"        
        return render(request, "reservations/reservations.html", {"error": error_message})



