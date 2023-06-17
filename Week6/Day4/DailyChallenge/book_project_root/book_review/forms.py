from django import forms
from .models import *

class SearchForm(forms.Form):
    title = forms.CharField(label='Title')
    
class BookReviewForm(forms.ModelForm):
   	class Meta:
            model = BookReview
            fields = 'associated_book', 'rating', 'review_text'
            widgets = {
            'rating': forms.RadioSelect
            }