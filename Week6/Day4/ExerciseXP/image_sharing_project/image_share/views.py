from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import RegisterForm, ImageForm
from django.contrib.auth.models import User
from .models import Image, Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
   form_class = RegisterForm
   model = User
   template_name = 'registration/register.html'
   success_url = reverse_lazy('registration/login')

# view images uploaded by other users
class AllImageListView(ListView) :
    model = Image
    template_name = 'image_share/feed.html'
    context_object_name = 'images'

# upload an images
class ImageCreateView(LoginRequiredMixin, CreateView) :
    model = Image
    form_class = ImageForm
    template_name = 'image_share/upload_image.html'
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# view their own uploaded images
class MyImageListView(LoginRequiredMixin, ListView) :
    model = Image
    template_name = 'image_share/my_images.html'
    context_object_name = 'images'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(upload_user=self.request.user)
        return queryset

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'image_share/profile.html'
    context_object_name = 'profiles'
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)