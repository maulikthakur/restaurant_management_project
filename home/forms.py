from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact        
        fields = ['name', 'email']
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            }

    
