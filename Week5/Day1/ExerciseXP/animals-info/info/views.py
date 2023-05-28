from django.shortcuts import render
import json
# Create your views here.

filename = 'Day1/ExerciseXP/animals-info/info/json_file.json'


with open("json_file.json", "r") as f:
    data = json.load(f)

animals = data['animals']
families = data['families']

def animal (request, id) :
    animal_selected = ''
    for i in animals :
        if i['id'] == id :
            animal_selected = i
    return render (request, 'animal.html', animal_selected)

def family (request, id) :
    family_selected = ''
    for i in family :
        if i['id'] == id :
            family_selected = i
    return render (request, 'family.html', family_selected)