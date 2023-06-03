from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self) :
	    return f'{self.first_name} {self.last_name}'
 
class Vehicle (models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete = models.CASCADE)
    date_created = models.DateField(auto_now=True)
    cost = models.FloatField()
    size = models.ForeignKey('VehicleSize', on_delete = models.CASCADE)

    def __str__(self) :
	    return self.vehicle_type
 
class VehicleType (models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) :
	    return self.name

class VehicleSize (models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) :
	    return self.name
 
class Rental (models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(null=True)
    customer = models.ForeignKey('Customer', on_delete = models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', on_delete = models.DO_NOTHING)
    
    def __str__(self) :
	    return f'{self.customer}, {self.rental_date}'
 
class RentalRate (models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey('VehicleType', on_delete = models.CASCADE)
    vehicle_size = models.ForeignKey('VehicleSize', on_delete = models.CASCADE)

    def __str__(self) :
	    return f'Rate for {self.vehicle_size} {self.vehicle_type}'
 
class RentalStation (models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()
    address = models.ForeignKey('Address', on_delete = models.CASCADE)

    def __str__(self) :
	    return self.name
 
class Address (models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    
    def __str__(self) :
	    return self.city