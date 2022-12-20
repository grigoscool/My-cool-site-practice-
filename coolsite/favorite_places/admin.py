from django.contrib import admin

from .models import *

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'img', 'people')
    list_display_links = ('name', 'id')
    prepopulated_fields = {'slug': ('name',)}

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'fst_name')
    list_display_links = ('id', 'fst_name')
    prepopulated_fields = {'slug': ('fst_name',)}

admin.site.register(Place, PlacesAdmin)
admin.site.register(People, PeopleAdmin)
