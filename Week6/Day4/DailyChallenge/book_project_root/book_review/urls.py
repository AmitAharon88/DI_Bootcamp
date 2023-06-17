from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', BookListView.as_view(), name='homepage'),
    path('bookdetails/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('search/', search, name='search'),
    path('review/<int:pk>', BookReviewCreateView.as_view(), name='review'),

]