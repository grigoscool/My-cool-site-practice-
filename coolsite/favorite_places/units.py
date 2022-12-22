menu = [
    {'title': "add place", 'url_name': 'add_place'},
    {'title': "about", 'url_name': 'about'},
    {'title': "contact", 'url_name': 'contact'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context