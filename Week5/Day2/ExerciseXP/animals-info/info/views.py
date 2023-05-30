from django.shortcuts import render
from .models import Animal, Family


def show_family (request, family_id) :
    animals = Animal.objects.filter(id=family_id)
    return render (request, 'families.html', {'animals': animals})

def show_animal (request, animal_id) :
    animal = Animal.objects.get(id=animal_id)
    return render (request, 'animal.html', {'animal': animal})

def show_all_animals (request) :
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'animals': animals})