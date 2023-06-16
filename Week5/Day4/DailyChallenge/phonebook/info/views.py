from django.shortcuts import render, redirect
from .models import Person
from .forms import *
# Create your views here.

def by_name(request, name_search: str):
    try:
        person = Person.objects.get(name=name_search)
    except Person.DoesNotExist:
        return render(request, 'searched_person.html', {'error_message': 'No person by that name'})
    context = {'person': person}
    return render(request, 'searched_person.html', context)

def by_number(request, phonenumber_search):
    try:
        person = Person.objects.get(phone_number=phonenumber_search)
    except Person.DoesNotExist:
        return render(request, 'searched_person.html', {'error_message': 'No person by that phone number'})
    context = {'person': person}
    return render(request, 'searched_person.html', context)

def search_by(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone_number = form.cleaned_data.get('phone_number')
            if name:
                return redirect('name', name_search=name)
            elif phone_number:
                return redirect('Phone_number', phonenumber_search=phone_number)
        else:
            form = PersonForm()
    else:
        form = PersonForm()
        
    return render(request, 'person_search.html', {'form': form})