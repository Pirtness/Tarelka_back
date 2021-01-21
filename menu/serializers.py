from rest_framework import serializers
from menu.models import Ingredient, Dish


class IngredientSerializer(serializers.ModelSerializer):
    dish_id = serializers.ReadOnlyField(source='dish_id.id')

    class Meta:
        model = Ingredient
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    ingredients_list = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = '__all__'
