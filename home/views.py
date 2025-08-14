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
        'restaurant_name': settings.restaurant_name,
        'restaurant_address': restaurant.address if restaurant and restaurant.address else 'Babariya Near Babariya Lake Road, Seoni, Madhya Pradesh (480661)'   
    }

    return render(request,'homes.html', context)

# views.py
from django.shortcuts import render

def contact_us(request):
    contact_info = {
        "phone": "+91 9876543210",
        "email": "info@restaurant.com",
        "address": "Babariya Near Babariya Lake Road, Seoni, Madhya Pradesh (480661)"
    }
    return render(request, "contact_us.html", {"contact_info": contact_info})



