from rest_framework import generics
from menu.models import Ingredient, Dish, DayMenu, WeekMenu
from menu.serializers import IngredientSerializer, DishSerializer, DayMenuSerializer, WeekMenuSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

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

class WeekMenuList(viewsets.ModelViewSet):

    #add permissions

    serializer_class = WeekMenuSerializer
    queryset = WeekMenu.objects.all()
    #http_method_names = ['get']

    @action(detail=False, methods=['POST'])
    def createMenu(self, request):

        weekMenus = WeekMenu.objects.filter(username=self.request.user,
                    startDate = datetime.datetime.now().date())
        if len(weekMenus) > 0:
            return Response(WeekMenuSerializer(weekMenus, many=True).data)

        WeekMenu.objects.create(username=self.request.user,
                startDate = datetime.datetime.now().date(),
                endDate = datetime.datetime.now().date() + datetime.timedelta(days=2))

        weekMenu = WeekMenu.objects.filter(username=self.request.user,
                    startDate = datetime.datetime.now().date())[0]

        #weekMenu.save()

        dish = Dish.objects.all()[0]

        daysInWeek = 3
        for i in range(daysInWeek):
            dayMenu = DayMenu(menu_id = weekMenu,
                    day = datetime.datetime.now().date() + datetime.timedelta(days = i),
                    breakfast = dish, dinner = dish, lunch = dish)
            dayMenu.save()
        return Response(WeekMenuSerializer(weekMenu).data)
