from rest_framework import generics
from menu.models import Ingredient, Dish, DayMenu
from menu.serializers import IngredientSerializer, DishSerializer, DayMenuSerializer
from rest_framework.response import Response

import datetime

class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer

    #def perform_create(self, serializer):

class DishList(generics.ListAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()

    def get_queryset(self):
        return queryset

class DayMenuList(generics.ListCreateAPIView):
    serializer_class = DayMenuSerializer
    queryset = DayMenu.objects.all()

    def perform_create(self, serializer):
        serializer.save(day = datetime.datetime.now().date() + datetime.timedelta(days=1))
