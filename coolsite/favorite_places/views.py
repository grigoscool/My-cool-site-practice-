from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

menu = [
    {'title':"about", 'url_name': 'about'},
    {'title': "contact", 'url_name': 'contact'}
]

def index(request):
    hotels = Place.objects.all()
    return render(request, 'index.html', {'hotels': hotels,'menu':menu})

def hotels(request):
    return render(request, 'hotels.html',{'menu':menu})

def hotel(request, hotel_id):

    return render(request, 'hotel.html',{'menu':menu})

def about(request):
    return render(request, 'about.html',{'menu':menu})

def contact(request):
    return render(request, 'contact.html',{'menu':menu})