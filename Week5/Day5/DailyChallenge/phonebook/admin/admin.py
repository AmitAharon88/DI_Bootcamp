from django.contrib import admin
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from .models import *

admin.site.register(PhoneNumberModelAdmin)
