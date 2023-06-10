from django import forms
from django.contrib.admin.widgets import AdminSearchWidget
from django.contrib.admin.views.main import SEARCH_VAR
from .models import PhoneNumberModel
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class PhoneNumberModelForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget)

    class Meta:
        model = PhoneNumberModel
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[SEARCH_VAR] = forms.CharField(
            required=False,
            widget=AdminSearchWidget(attrs={'placeholder': 'Search'}),
        )