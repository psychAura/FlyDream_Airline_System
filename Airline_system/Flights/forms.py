# forms.py
from django import forms
from .models import GuestBooking

class GuestBookingForm(forms.ModelForm):
    class Meta:
        model = GuestBooking
        fields = ['first_name', 'last_name', 'email',]
            #### styling input fields here because tailwind css can't style django forms directly.
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-black rounded',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-black rounded',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-black rounded',
                'placeholder': 'you@example.com'
            }),
            }
