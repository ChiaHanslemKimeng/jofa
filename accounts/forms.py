from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'country']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
            'address': forms.Textarea(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
            'country': forms.TextInput(attrs={'class': 'w-full border border-gray-100 p-4 font-light text-sm outline-none focus:border-jofa-gold transition-colors'}),
        }
