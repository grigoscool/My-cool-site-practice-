from django import template
from favorite_places.models import Place, People


register = template.Library()

@register.simple_tag()
def get_people():
    return People.objects.all()

@register.inclusion_tag('list_people.html')
def show_people():
    people = People.objects.all()
    return {'people':people}
