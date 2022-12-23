import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Place, People
from .forms import AddPlaceForm, RegisterForm
from .units import *

def index(request):
    hotels = Place.objects.all()
    return render(request, 'index.html', {'hotels': hotels, 'menu': menu})

@login_required(login_url = '/admin/')    # декоратор проверяет залогинен ли пользователь
def hotels(request):
    r_hotels = []
    while len(r_hotels) != 3:
        r_hotel = Place.objects.get(id=random.randint(1,7))
        if r_hotel not in r_hotels:
            r_hotels.append(r_hotel)
    return render(request, 'hotels.html',{'menu':menu, 'r_hotels':r_hotels})


class Hotel(DataMixin, DetailView):
    model = Place
    template_name = 'hotel.html'
    context_object_name = 'hotel'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавляем словарь из units из класса DataMixin
        user_cont = self.get_user_context()
        # возвращаем сумму словарей
        return context | user_cont

class AddPlace(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPlaceForm
    template_name = 'add_place.html'
    # переменная определят куда перенаправит не авторизованного пользователя добавляет страницу
    login_url = reverse_lazy('index')
    raise_exception = True
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cont = self.get_user_context()
        return context | user_cont



class About(DataMixin, TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add menu from the top
        user_cont = self.get_user_context()
        return context | user_cont

class Contact(DataMixin, TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cont = self.get_user_context()
        return context | user_cont

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

def login(request):
    return render(request, 'login.html')

class RegaisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cont = self.get_user_context()
        return context | user_cont

