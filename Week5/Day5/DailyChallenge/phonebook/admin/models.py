from django.db import models
from forms import *
from admin import *

# Create your models here.
class PhoneNumberModelAdmin(admin.ModelAdmin):
    form = PhoneNumberModelForm
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('phone_number', 'email', 'name')
    exclude = ('id',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(phone_number__contains=search_term)
        return queryset, use_distinct