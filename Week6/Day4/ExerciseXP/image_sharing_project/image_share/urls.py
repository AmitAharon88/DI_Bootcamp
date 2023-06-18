from django.urls import path
from django.contrib.auth import views
from .views import RegisterView, AllImageListView, ImageCreateView, MyImageListView, ProfileListView

urlpatterns = [
   path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout'),
   path('register/', RegisterView.as_view(), name='register'),
   path('feed/', AllImageListView.as_view(), name='feed'),
   path('upload-image/', ImageCreateView.as_view(), name='upload-image'),
   path('my-images/', MyImageListView.as_view(), name='my-images'),
   path('profile/', ProfileListView.as_view(), name='profile'),
]