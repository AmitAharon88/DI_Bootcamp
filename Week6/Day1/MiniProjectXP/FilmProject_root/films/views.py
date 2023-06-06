from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm
from django.urls import reverse_lazy
from django.views.generic import ListView
# Create your views here.

class HomePageView(ListView) :
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'
    success_url = reverse_lazy('homepage')
    
class FilmCreateView(CreateView) :
    model = Film
    form_class = FilmForm
    template_name = 'film/addfilm.html'
    success_url = reverse_lazy('addfilm')

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/adddirector.html'
    success_url = reverse_lazy('adddirector')

class ReviewCreateView(CreateView) :
    model = Review
    form_class = ReviewForm
    template_name = 'review/addreview.html'
    success_url = reverse_lazy('addreview')
    