import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import Rental, Vehicle, Customer
from faker import Faker
from random import choice
from datetime import datetime, timedelta

def create_rentals(number):
    faker = Faker()
    vehicles = list(Vehicle.objects.all())
    rented_vehicles = set()
    
    for _ in range(number):
        rental_date = faker.date_time_between(start_date='-60d', end_date='now')
        return_date = None
        
        if choice([True, False]):
            return_date = faker.date_time_between(start_date=rental_date, end_date=datetime.now())
        
        customer = choice(Customer.objects.all())
        vehicle = choice(vehicles)
        
        while vehicle in rented_vehicles:
            vehicle = choice(vehicles)

        rented_vehicles.add(vehicle)
        
        rental = Rental(
                rental_date = rental_date,
                return_date = return_date,
                customer = customer,
                size = vehicle
        )
        rental.save()

    print(f"CREATED {number} Rentals")

create_rentals(100)