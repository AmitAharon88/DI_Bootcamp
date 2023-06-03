from django import forms
from .models import Customer, Vehicle
 
class CreateRentalForm(forms.Form):
    customer_id = forms.IntegerField(label='Customer ID')
    vehicle_id = forms.IntegerField(label='Vehicle ID')

class CreateCustomerForm(forms.Form):
    class Meta:
        model = Customer
        fields = '_all_'

class CreateVehicleForm(forms.Form):
    class Meta:
        model = Vehicle
        fields = '_all_'