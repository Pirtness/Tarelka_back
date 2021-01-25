from django.urls import path, include
from menu import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('dish/', views.DishList.as_view()),
    path('daymenu/', views.DayMenuList.as_view()),
    #path('menu/', views.WeekMenuList.as_view()),
]

router = DefaultRouter()
router.register(r'menu', views.WeekMenuList)

urlpatterns += [
    path('', include(router.urls)),
]
