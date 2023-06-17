from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from .models import Booking, RoomType
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

    def confirm(request, pk = None):
        if request.method == 'POST':
            if pk:
                invalid_dates = False
                # get the room 
                room = RoomType.objects.get(pk = pk)
                guest_id = request.user
                check_in = request.session['check_in'] 
                check_out = request.session['check_out']

                # check wether the dates are valid
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Booking.objects.filter(room=room, check_in__lte=check_in, check_out__gte=check_in).exists()

            # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Booking.objects.filter(room=room, check_in__lte=check_out, check_out__gte=check_out).exists()
            
            case_3 = Booking.objects.filter(room=room, check_in__gte=check_in, check_out__lte=check_out).exists()


            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                  return render(request, "system/reserve.html", {"errors": "This room is not available on your selected dates"})                  
            
            # dates are valid             
            reservation = Booking(
                check_in = check_in, 
                check_out = check_out,
                room_id = room.id,
                guest_id = guest_id.id
             )
            reservation.save()
             #redirect to success page (need to define this as a separate view)
            return redirect("/reservation_success")

        return render(request, "/booking", args)
'''
If guest check in date >= check in date or guest check out date <= check out date --> wont be able to book

guest 1- 5-10/7
guest 2- 1-12/7
'''


    # def get_queryset(self) :
    #     return super().get_queryset('check_in_date', 'check_out_date')