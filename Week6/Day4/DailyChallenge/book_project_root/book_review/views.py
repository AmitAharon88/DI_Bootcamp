from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.

# class BookListView(ListView) : ---> DON'T NEED
#     model= Book
#     template_name = 'view_books.html'
#     context_object_name = 'books'
#     succedd_url = 'view_books'