import random

from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Place, People
from .forms import AddPlaceForm

menu = [
    {'title':"add place", 'url_name': 'add_place'},
    {'title':"about", 'url_name': 'about'},
    {'title': "contact", 'url_name': 'contact'}
]

def index(request):
    hotels = Place.objects.all()
    return render(request, 'index.html', {'hotels': hotels,'menu':menu})

def hotels(request):
    r_hotels = []
    while len(r_hotels) != 3:
        r_hotel = Place.objects.get(id=random.randint(1,7))
        if r_hotel not in r_hotels:
            r_hotels.append(r_hotel)
    return render(request, 'hotels.html',{'menu':menu, 'r_hotels':r_hotels})

def hotel(request, hotel_slug):
    hotel = Place.objects.get(slug=hotel_slug)
    return render(request, 'hotel.html',{'menu':menu,'hotel':hotel})

def add_place(request):

    if request.method == 'POST':                #есди данные введены
        form = AddPlaceForm(request.POST)       #экземпляр заполняется ими
        if form.is_valid():                     #проверка на соотв условиям
            print(form.cleaned_data)
    else:
        form = AddPlaceForm()                   #если данных нет, пустая форма

    return render(request, 'add_place.html', {'form':form, 'menu':menu})

def about(request):
    return render(request, 'about.html',{'menu':menu})

def contact(request):
    return render(request, 'contact.html',{'menu':menu})

def people(request, people_slug):
    ex = People.objects.get(slug=people_slug)
    hotels = Place.objects.filter(people_id=ex.id)
    context = {
        'hotels': hotels,
        'menu': menu,
    }
    if len(hotels) == 0:
        raise Http404()

    return render(request, 'people.html', context)