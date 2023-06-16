from django import forms
from .models import Film, Director, Review, Producer
from django.utils import timezone
# from django.forms import formset_factory

class FilmForm(forms.ModelForm):
   	class Meta:
            model = Film
            fields = '__all__'
            widgets = {
                'release_date': forms.DateInput(attrs={'type': 'date'})
            }
# allows you to choose a date from the options instead of writting it        
    # def clean_release_date(self):
    #     today = timezone.now().date()
    #     release_date = self.clean_data.get('release_date')
    #     if release_date > today :
    #         raise forms.ValidationError("Release date can not be in the future!")
    #     return release_date
        
class DirectorForm(forms.ModelForm):
   	class Meta:
            model = Director
            fields = '__all__'

class ReviewForm(forms.ModelForm):
   	class Meta:
            model = Review
            fields = 'film', 'review_text', 'rating'
            widgets = {
            'rating': forms.RadioSelect
            }

# class ProducerForm(forms.ModelForm):
#    	class Meta:
#             model = Producer
#             fields = '__all__'
#             widgets = {
#             'rating': forms.RadioSelect
#             }

# ProducerFormSet = formset_factory(model=Producer, form=ProducerForm, extra=0)