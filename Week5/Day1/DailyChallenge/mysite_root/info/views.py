from django.shortcuts import render
import json
# Create your views here.
with open('/Users/amitaharon/Documents/Developers_Institute/DI_Bootcamp/Week5/Day1/DailyChallenge/mysite_root/info/people.json', "r") as people :
        data = json.load(people)


def all_people_view (request) :
    people_sorted = sorted(data, key =  lambda person: person['age'])
    context = {'people': people_sorted}
    return render(request, 'allPeople.html', context)

def person_view (request, id: int) :
    person_selected = ''
    for i in data :
        if i['id'] == id :
            person_selected = i
            break
    context = {'person_instance': person_selected}
    return render (request, 'singlePerson.html', context)