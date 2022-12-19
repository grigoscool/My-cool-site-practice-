import random

from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Place, People

menu = [
    {'title':"about", 'url_name': 'about'},
    {'title': "contact", 'url_name': 'contact'}
]

def index(request):
    hotels = Place.objects.all()
    people = People.objects.all()
    return render(request, 'index.html', {'hotels': hotels,'menu':menu, 'people':people})

def hotels(request):
    r_hotels = []
    while len(r_hotels) != 3:
        r_hotel = Place.objects.get(id=random.randint(1,7))
        if r_hotel not in r_hotels:
            r_hotels.append(r_hotel)
    return render(request, 'hotels.html',{'menu':menu, 'r_hotels':r_hotels})

def hotel(request, hotel_id):

    return render(request, 'hotel.html',{'menu':menu})

def about(request):
    return render(request, 'about.html',{'menu':menu})

def contact(request):
    return render(request, 'contact.html',{'menu':menu})

def people(request, people_id):
    hotels = Place.objects.filter(people_id=people_id)
    people = People.objects.all()
    context = {
        'hotels': hotels,
        'menu': menu,
        'people': people,
    }
    if len(hotels) == 0:
        raise Http404()

    return render(request, 'people.html', context)