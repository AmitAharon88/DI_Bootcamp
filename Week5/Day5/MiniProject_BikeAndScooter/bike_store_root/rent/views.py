from django.shortcuts import render, redirect
from django.contrib import messages
from.models import *
from rent.forms import CreateRentalForm, CreateCustomerForm, CreateVehicleForm

def show_rentals (request) :
    rentals = Rental.objects.order_by('return_date', 'rental_date')
    context = {'rentals': rentals}
    return render(request, 'rental_list.html', context)

def rental_detail(request, pk):
    try:
        rental = Rental.objects.get(pk=pk)
        context = {'rental': rental}
        return render(request, 'rental_details.html', context)
    except Rental.DoesNotExist:
        messages.error(request, 'Rental does not exist.')
        return redirect('show_rentals')

def create_rental(request):
    form = CreateRentalForm()
    
    if request.method == 'POST':
        form = CreateRentalForm(request.Post)
        
        if form.is_valid():
            customer_id = form.cleaned_data['customer_id']
            vehicle_id = form.cleaned_data['vehicle_id']
        
            try:
                customer = Customer.objects.get(id=customer_id)
                vehicle = Vehicle.objects.get(id=vehicle_id)
            
                if vehicle.is_rented():
                    messages.error(request, 'Vehicle is currently being rented.')
                else:
                    rental = Rental(customer=customer, vehicle=vehicle)
                    rental.save()
                    messages.success(request, 'Rental created successfully.')
                    return redirect('show_rentals')
        
            except Customer.DoesNotExist:
                messages.error(request, 'Invalid customer ID.')
        
            except Vehicle.DoesNotExist:
                messages.error(request, 'Invalid vehicle ID.')
    
    return render(request, 'create_rental.html')

def show_customer(request):
    customers = Customer.objects.order_by('last_name')
    context = {'customers': customers}
    return render(request, 'customer_list.html', context)

def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        context = {'customer': customer}
        return render(request, 'customer_details.html', context)
    except Customer.DoesNotExist:
        messages.error(request, 'Customer does not exist.')
        return redirect('show_customer')
    
def create_customer(request):
    form = CreateCustomerForm()

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer created successfully.')
            return redirect('show_customer')
    
    context = {'form': form}
    return render(request, 'create_customer.html', context)

def show_vehicle(request):
    vehicles = Vehicle.objects.all()
    vehicle_types = VehicleType.objects.all().order_by('name')
    context ={'vehicles': vehicles,
              'vehicle_types': vehicle_types,
                }
    return render(request, 'vehicle_list.html', context)

def vehicle_detail(request, pk):
    try:
        vehicle = Vehicle.objects.get(pk=pk)
        is_rented = Rental.objects.filter(vehicle=vehicle, return_date=None).exists()
        context = {'vehicle': vehicle, 'is_rented': is_rented}
        return render(request, 'vehicle_detail.html', context)
    except Vehicle.DoesNotExist:
        messages.error(request, 'Vehicle does not exist.')
        return redirect('show_vehicle')

def create_vehicle(request):
    if request.method == 'POST':
        form = CreateVehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_vehicles')
    else:
        form = CreateVehicleForm()

    context = {'form': form}
    return render(request, 'create_vehicle.html', context)