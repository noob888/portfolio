# forms.py
from django import forms
from .models import ContactModel, HomeContactModel

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'message']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'message': 'Message'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomeContactModel
        fields = ['email']
        labels = {'email': 'Email'}
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }
