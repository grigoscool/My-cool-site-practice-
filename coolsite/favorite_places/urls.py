from django.urls import path
from favorite_places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/', views.hotel, name='sigl'),
    path('hotels/', views.hotels, name='hotels'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hotels/<int:hotel_id>/', views.hotel, name='hotel'),
    path('people/<int:people_id>/', views.people, name='people'),
]