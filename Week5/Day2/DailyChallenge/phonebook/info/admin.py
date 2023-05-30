from django.contrib import admin
from .models import Person
# Register your models here.
admin.site.register(Person)

# 1. python manage.py createsuperuser
# 2. in admin.py -> 
#                   1. import model
#                   2. admin.site.register(model)