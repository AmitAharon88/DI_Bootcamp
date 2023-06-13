from django import forms
from phonenumber_field.formfields import PhoneNumberField

class PersonForm(forms.Form):
    name = forms.CharField(label='Name', required=False)
    phone_number = PhoneNumberField(label='Phone Number', required=False)
