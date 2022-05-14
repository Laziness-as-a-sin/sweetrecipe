from django.urls import path
from .views import *


urlpatterns = [
    path('', RecipeHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('addrecipe/', AddRecipe.as_view(), name='addrecipe'),
]