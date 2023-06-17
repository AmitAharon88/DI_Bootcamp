from django.shortcuts import render
from .models import Booking
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def info_page(request) :
    return render (request, 'infopage.html')

class BookingView(CreateView) :
    model = Booking
    template_name = 'booking.html'
    fields = ['guest_name','check_in_date', 'check_out_date', 'num_guests', 'room']
    success_url = reverse_lazy('booking')