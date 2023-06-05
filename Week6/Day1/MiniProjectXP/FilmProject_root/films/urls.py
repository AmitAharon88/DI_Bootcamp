from django.urls import path
from films.views import *

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('addfilm/', FilmCreateView.as_view(), name='addfilm'),
    path('adddirector/', DirectorCreateView.as_view(), name='adddirectory')
]