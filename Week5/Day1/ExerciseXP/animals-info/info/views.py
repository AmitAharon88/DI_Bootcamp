from django.shortcuts import render
import json
import os
# Create your views here.

filename = '/Users/amitaharon/Documents/Developers_Institute/DI_Bootcamp/Week5/Day1/ExerciseXP/animals-info/info/json_file.json'


with open(filename, "r") as f:
    data = json.load(f)

animals = data['animals']
families = data['families']

def animal (request, id) :
    animal_selected = ''
    for i in animals :
        if i['id'] == id :
            animal_selected = i
    return render (request, 'animals.html', animal_selected)

def family (request, id) :
    family_selected = ''
    for i in families :
        if i['id'] == id :
            family_selected = i
    return render (request, 'families.html', family_selected)