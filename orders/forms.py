from django import forms
from orders.validators import PhoneNumberValidator, ZipCodeValidator


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'})
    )
    phone = forms.CharField(
        validators=[PhoneNumberValidator(10)],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    address_line = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'})
    )
    zip_code = forms.CharField(
        validators=[ZipCodeValidator(4)],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'})
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Additional Notes (optional)',
            'rows': 3
        })
    )
