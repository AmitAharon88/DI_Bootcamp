from django.contrib import admin
from django.urls import path
from rent.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', show_rentals, name='show_rentals'),
    path('rental/<int:pk>', rental_detail, name='rental_details'),
    path('rental/add/', create_rental, name='create_rental'),
    path('customer/', show_customer, name='show_customers'),
    path('customer/<int:pk>', customer_detail, name='customer_details'),
    path('customer/add/', create_customer, name='create_customer'),
    path('vehicle/', show_vehicle, name='show_vehicle'),
    path('vehicle/<int:pk>', vehicle_detail, name='vehicle_details'),
    path('vehicle/add/', create_vehicle, name='create_vehicle'),
]
