from .models import *



menu = [
    {'title': "Добавить рецепт", 'url_name': 'addrecipe'},
    {'title': "О нас", 'url_name': 'about'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context