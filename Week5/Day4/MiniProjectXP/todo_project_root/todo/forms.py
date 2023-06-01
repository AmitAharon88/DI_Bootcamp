from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # category_field = forms.ChoiceField(choice=[])
        fields = ('title', 'details', 'deadline_date', 'category')
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'})
        }
        
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['category'].choices = self.get_category_choices()

        # def get_category_choices(self):
        #     categories = Category.objects.all()
        #     return [(category.id, category.name) for category in categories]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DoneForm(forms.Form):
    instance = forms.ModelChoiceField(queryset=Todo.objects.all(),
                                      widget=forms.HiddenInput())