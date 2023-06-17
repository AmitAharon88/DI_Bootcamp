from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    published_date= models.DateField()
    description= models.TextField()
    page_count= models.IntegerField()
    categories= models.CharField(max_length=200)
    thumbnail_url= models.URLField()

    def __str__(self):
        return self.title
    
class BookReview(models.Model):
    associated_book= models.ForeignKey(Book, on_delete=models.CASCADE, related_name= 'reviews')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text= models.TextField()
    
    def __str__(self):
        return f"Review for {self.associated_book.title} by {self.user.username}"