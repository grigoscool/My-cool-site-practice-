menu = [
    {'title': "add place", 'url_name': 'add_place'},
    {'title': "about", 'url_name': 'about'},
    {'title': "contact", 'url_name': 'contact'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        new_menu = menu.copy()
        if not self.request.user.is_authenticated:
            new_menu.pop(0)

        context['menu'] = new_menu
        return context