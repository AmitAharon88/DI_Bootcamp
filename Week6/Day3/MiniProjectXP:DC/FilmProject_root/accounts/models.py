from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='profile')
    
    def __str__(self):
        return f'Profile: {self.user.username}'

# FOR W6D2 XP ---> NOT WORKING FOR ME
# class CustomUser(AbstractBaseUser) :
#     username = models.CharField(max_length=150, unique=True)
#     birthday = models.DateField()
#     favorite_film = models.CharField(max_length=100)
#     favorite_actor = models.CharField(max_length=100)
#     USERNAME_FIELD = 'username'

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, birthday, favorite_film, favorite_actor, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set.")
        
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             birthday=birthday,
#             favorite_film=favorite_film,
#             favorite_actor=favorite_actor,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, birthday, favorite_film, favorite_actor, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
        
#         return self.create_user(email, birthday, favorite_film, favorite_actor, password, **extra_fields)