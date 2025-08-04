from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to clear the form
        else:
            form = ContactForm()

    return render(request,"homes.html")

