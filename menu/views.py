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



class WeekMenuList(viewsets.ViewSet):

    daysInWeek = 7
    #add permissions

    queryset = WeekMenu.objects.all()
    #http_method_names = ['get']



    def list(self, request):
        weekMenus = WeekMenu.objects.filter(username=self.request.user,
                         endDate__gt = datetime.datetime.now().date())


        if len(weekMenus) == 1:
            sDate = weekMenus[0].endDate + datetime.timedelta(days=1)
            self.createMenu(self.request.user, sDate)
        elif len(weekMenus) == 0:
            sDate = datetime.datetime.now().date()
            weekMenu = self.createMenu(self.request.user, sDate)
            sDate = weekMenu.endDate + datetime.timedelta(days=1)
            self.createMenu(self.request.user, sDate)
        else:
            serializer = WeekMenuSerializer(weekMenus, many=True)
            return Response(serializer.data)


        weekMenus = WeekMenu.objects.filter(username=self.request.user,
                         endDate__gt = datetime.datetime.now().date())

        serializer = WeekMenuSerializer(weekMenus, many=True)
        return Response(serializer.data)



    # @action(detail=False, methods=['POST'])
    def createMenu(self, user, sDate):
        WeekMenu.objects.create(username=user, startDate = sDate,
                endDate = sDate + datetime.timedelta(days=self.daysInWeek))

        weekMenu = WeekMenu.objects.filter(username=user, startDate = sDate,
                endDate = sDate + datetime.timedelta(days=self.daysInWeek))[0]

        dish = Dish.objects.all()[0]

        for i in range(self.daysInWeek):
            dayMenu = DayMenu(menu_id = weekMenu,
                    day = sDate + datetime.timedelta(days = i),
                    breakfast = dish, dinner = dish, lunch = dish)
            dayMenu.save()

        return weekMenu
