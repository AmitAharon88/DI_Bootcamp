from django import forms
from .models import Gif, Category

class GifForm(forms.ModelForm) :
    class Meta:
        model= Gif
        fields= 'uploader_name', 'title', 'url'
        widgets = {
            'category': forms.MultipleChoiceField
        }
# categories : look up ModelMultipleChoiceField

class CategoryForm(forms.ModelForm) :
    class Meta:
        model= Category
        fields= ['name']