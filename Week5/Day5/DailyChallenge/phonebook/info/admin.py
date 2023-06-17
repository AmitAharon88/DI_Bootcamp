from django.contrib import admin
from .models import Person
# Register your models here.
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class PhoneRegion(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']
    list_editable = ['phone_number']
    formfield_overrides = {
        PhoneNumberField: {"widget": PhoneNumberPrefixWidget},
    }
    search_fields = ('name', 'email', 'phone_number')
    
admin.site.register(Person, PhoneRegion)