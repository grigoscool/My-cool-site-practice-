from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

def index(request):
    return render(request, 'index.html')

def hotels(request):
    return render(request, 'hotels.html')

def hotel(request):
    return render(request, 'hotel.html')