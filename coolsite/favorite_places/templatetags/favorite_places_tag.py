from django import template
from favorite_places.models import Place, People


register = template.Library()

@register.simple_tag()
def get_people():
    return People.objects.all()
