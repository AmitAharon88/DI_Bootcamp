from django.contrib import admin
from django.urls import path
from films.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('addfilm/', FilmCreateView.as_view(), name='addfilm'),
    path('adddirector/', DirectorCreateView.as_view(), name='adddirectory')
]
