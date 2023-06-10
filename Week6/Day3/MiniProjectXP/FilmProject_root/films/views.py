from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView
from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

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
    success_url = reverse_lazy('homepage')

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/adddirector.html'
    success_url = reverse_lazy('homepage')
    
class ReviewCreateView(CreateView) :
    model = Review
    form_class = ReviewForm
    template_name = 'review/addreview.html'
    success_url = reverse_lazy('homepage')
    
class DeleteFilmView(UserPassesTestMixin, DeleteView) :
    model = Film
    success_url = reverse_lazy('homepage')
    template_name = 'film/deletefilm.html'
    
    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Film deleted successfully!')
        return super().delete(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.none()
        return queryset