from django.shortcuts import render
from people import *
# Create your views here.
filename = 'Day1/DailyChallenge/mysite_root/info/people.py'


with open(filename, "r") as p:
    p.read()

def all_people_view (request) :
    people = people.objects.order_by('age')
    context = {'people': people}
    return render(request, 'people.html', context)

def person_view (request, id) :
    person_selected = ''
    for i in people :
        if i['id'] == id :
            person_selected = i
    return render (request, 'singlePerson.html', person_selected)