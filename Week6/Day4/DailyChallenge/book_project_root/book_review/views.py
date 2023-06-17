from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView, ListView, DetailView
from .forms import *
from django.urls import reverse_lazy
from django.db.models import Avg, Count
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BookListView(ListView) :
    model= Book
    template_name = 'homepage.html'
    context_object_name = 'books'
    succedd_url = 'homepage'

class BookDetailView (DetailView) :
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['book']
        book_avg_rating = book.reviews.aggregate(avg_rating=Avg('rating'))
        book_num_reviews = book.reviews.aggregate(num_reviews=Count('id'))

        context['avg_rating'] = book_avg_rating['avg_rating']
        context['num_reviews'] = book_num_reviews['num_reviews']
        return context

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if title:
                try:
                    book = Book.objects.get(title=title)
                    context = {'book': book}
                    return render(request, 'book_details.html', context)
                except Book.DoesNotExist:
                    return render(request, 'searched_book.html', {'error_message': 'No book with that title found'})
    else:
        form = SearchForm()
    return render(request, 'search_book.html', {'form': form})

class BookReviewCreateView(LoginRequiredMixin, CreateView) :
    model = BookReview
    form_class = BookReviewForm
    template_name = 'book_review.html'
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)