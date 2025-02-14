from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)


def __init__(self, *args, **kwargs):
    """
    Add placeholders to field options and
    set autofocus to name field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email Address',
        'phone_number': 'Phone Number',
        'country': 'Country',
        'postcode': 'Postal Code',
        'town_or_city': 'Town/City',
        'street_address1': 'Street Address 1',
        'street_address2': 'Street Address 2',
        'county': 'County',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    self.fields['country'].label = "Country code (e.g US, IE)"
    self.fields['street_address1'].label = "Street address (line 1)"
    self.fields['street_address2'].label = "Street address (line 2)"
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
