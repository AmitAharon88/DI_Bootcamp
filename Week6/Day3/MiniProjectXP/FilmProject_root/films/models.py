from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Country(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class Category(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class Director(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) :
        return f'{self.first_name} {self.last_name}'
    
class Film(models.Model) :
    title = models.CharField(max_length=50)
    release_date = models.DateField(default=timezone.now().date())
    created_in_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='films_created')
    available_in_countries = models.ManyToManyField(Country, related_name='films_available')
    category = models.ManyToManyField(Category, related_name= 'films')
    director = models.ManyToManyField(Director, related_name= 'films')
    # producers = models.ManyToManyField('Producer', related_name= 'films')

    def __str__(self) :
        return self.title

class Review(models.Model) :
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'author', blank=True, null=True)
    
    def __str__(self) :
        return self.film. title

class Producer(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     
# class UserNew(AbstractUser):
#     favorite_films = models.ManyToManyField('Film', related_name='users_fav', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='account', blank=True)
#     user_groups = models.ManyToManyField(Group, related_name='user_accounts', blank=True)