from django.contrib import admin
from menu.models import Ingredient, Dish, DayMenu, WeekMenu, Preference

admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(DayMenu)
admin.site.register(WeekMenu)
admin.site.register(Preference)
