from django.shortcuts import render
# Create your views here.
from people import people

with open(filename, "r") as p:
    p.read()

def all_people_view (request) :
    people_sorted = sorted(people, key =  lambda person: person['age'])
    context = {'people': people_sorted}
    return render(request, 'allPeople.html', context)

def person_view (request, id: int) :
    person_selected = ''
    for i in people :
        if i['id'] == id :
            person_selected = i
            break
        context = {'person_instance': person_selected}
    return render (request, 'singlePerson.html', context)