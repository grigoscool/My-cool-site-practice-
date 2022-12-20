from django import template
from favorite_places.models import Place, People


register = template.Library()

@register.simple_tag()
def get_people(filter=None):     #  в функцию передаем можно передавать параметры, которые исп дальше
    if not filter:
        return People.objects.all()
    else:
        return People.objects.filter(pk=filter)

@register.inclusion_tag('list_people.html')
def show_people(sort=None):     #в шаблоне в тэге указана переменная sort=имени человека
    if not sort:
        people = People.objects.all()
    else:
        people = People.objects.order_by(sort)
    return {'people':people}
