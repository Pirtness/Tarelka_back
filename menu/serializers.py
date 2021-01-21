from rest_framework import serializers
from menu.models import Ingredient, Dish, DayMenu
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class DayMenuSerializer(serializers.ModelSerializer):
    breakfast = serializers.ReadOnlyField(source='breakfast.id')
    lunch = serializers.ReadOnlyField(source='lunch.id')
    dinner = serializers.ReadOnlyField(source='dinner.id')

    class Meta:
        model = DayMenu
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    dish_id = serializers.ReadOnlyField(source='dish_id.id')

    class Meta:
        model = Ingredient
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    ingredients_list = IngredientSerializer(many=True)
    breakfasts = DayMenuSerializer(many=True)
    lunches = DayMenuSerializer(many=True)
    dinners = DayMenuSerializer(many=True)

    class Meta:
        model = Dish
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = get_user_model
        fields = '__all__'
