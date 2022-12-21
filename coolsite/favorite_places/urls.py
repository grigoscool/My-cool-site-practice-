from django.urls import path
from favorite_places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/', views.hotel, name='sigl'),
    path('hotels/', views.hotels, name='hotels'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
    path('hotels/<slug:hotel_slug>/', views.hotel, name='hotel'),
    path('people/<slug:people_slug>/', views.people, name='people'),
    path('add_place/', views.add_place, name='add_place'),
]