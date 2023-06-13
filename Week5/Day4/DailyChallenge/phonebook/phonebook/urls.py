from django.contrib import admin
from django.urls import path
from info.views import by_name, by_number, search_by

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/phonenumber/<str:phonenumber_search>', by_number, name= 'Phone_number'),
    path('persons/name/<str:name_search>', by_name, name= 'name'),
    path('persons-search/', search_by, name= 'search_by')
]
