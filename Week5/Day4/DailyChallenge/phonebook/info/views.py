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

def search_by(request) :
     if request.method == 'POST':
        form = request.POST
        filled_form = PersonForm(form)
        if form.is_valid():
            data= filled_form.cleaned_data
            if data['phonenumber'] :
                return redirect('phonenumber', phonenumber=data['phonenumber'])
            elif data['name']:
                return redirect('name', name=data['name'])
        else:
            form = PersonForm()
            context = {'form': form}
        return render(request, 'person_search.html', context)