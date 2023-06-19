from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image

class RegisterForm(UserCreationForm):
   class Meta:
       model = User
       fields = ['username', 'password1', 'password2']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image_file', 'upload_user']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }