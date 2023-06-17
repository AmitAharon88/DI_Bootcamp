from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookReview, Book
from django.db.models import Avg

@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, created, **kwargs):
    book = instance.associated_book
    average_rating = book.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    book.rating = average_rating
    book.save()