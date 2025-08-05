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

        context = {
            'form': form,
            'restaurant_name': settings.restaurant_name    
        }
    return render(request, 'homes.html', context)

                                                                                }

