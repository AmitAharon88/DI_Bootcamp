from django.urls import path
from .views import *

urlpatterns = [
    path('info_page/', info_page, name='info_page'),
    path('booking/', BookingView.as_view(), name='booking'),
]