
from django.views.generic import ListView, TemplateView
from django.shortcuts import render

from .models import *
from .utils import *




class RecipeHome(DataMixin, ListView):
    model = Dessert
    template_name = 'recipe/home.html'
    context_object_name = 'desserts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        for title in Dessert.objects.filter():
            category = Category.objects.filter(desserts__title=title)
            print(category)
            

        c_def = self.get_user_context(title="Главная", category = category)
        return dict(list(context.items()) + list(c_def.items()))
    

class About(DataMixin, TemplateView):
    template_name = 'recipe/about.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return dict(list(context.items()) + list(c_def.items()))


class AddRecipe(DataMixin, TemplateView):
    template_name = 'recipe/addrecipe.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рецепт")
        return dict(list(context.items()) + list(c_def.items()))
