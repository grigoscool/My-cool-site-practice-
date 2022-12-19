from django.contrib import admin

from .models import Place, People

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'img', 'people')
    list_display_links = ('name', 'id')

admin.site.register(Place, PlacesAdmin)
admin.site.register(People)
