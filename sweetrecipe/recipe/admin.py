from django.contrib import admin

from .models import *


admin.site.register(Dessert)
admin.site.register(Recipe)
admin.site.register(Category)