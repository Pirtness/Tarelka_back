from django.urls import path, include
from menu import views

urlpatterns = [
    path('dish/', views.DishList.as_view()),
]