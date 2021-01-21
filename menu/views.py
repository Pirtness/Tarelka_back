from rest_framework import generics
from menu.models import Ingredient, Dish
from menu.serializers import IngredientSerializer, DishSerializer
from rest_framework.response import Response


class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer

    #def perform_create(self, serializer):

class DishList(generics.ListAPIView):
    serializer_class = DishSerializer


    def get_queryset(self):
        queryset = Dish.objects.all()
        return queryset
