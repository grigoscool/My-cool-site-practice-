from django.urls import path
from favorite_places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/', views.Hotel.as_view(), name='sigl'),
    path('hotels/', views.hotels, name='hotels'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('hotels/<slug:slug>/', views.Hotel.as_view(), name='hotel'),
    path('people/<slug:people_slug>/', views.people, name='people'),
    path('add_place/', views.AddPlace.as_view(), name='add_place'),
]