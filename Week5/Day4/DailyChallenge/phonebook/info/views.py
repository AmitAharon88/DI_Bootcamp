from django.shortcuts import render
from .models import Person
from .forms import *
# Create your views here.

def by_name(request, name_search: str):
    person = None
    try:
        person = Person.objects.get(name=name_search)
    except Person.DoesNotExist:
        pass
    context = {'person': person}
    return render(request, 'search.html', context)

def by_number(request, phonenumber: str):
    person = None
    try:
        person = Person.objects.get(phone_number=phonenumber)
    except Person.DoesNotExist:
        pass
    context = {'person': person}
    return render(request, 'search.html', context)

# def search_by(request) :
#      if request.method == 'POST':
#         form = request.POST
#         filled_form = PersonForm(form)
#         filled_form.save()
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             name = form.cleaned_data['name']

#             if phone_number :
#                 people = Person.objects.filter(phone_number=phone_number)
#             elif name :
#                 people = Person.objects.filter(name__icontains=name)
#             else:
#                 people = Person.objects.none()

#             return render(request, 'person_search_results.html', {'people': people, 'form': form})
    
#         else:
#             form = PersonForm()
#             context = {'form': form}
#         return render(request, 'person_search.html', context)