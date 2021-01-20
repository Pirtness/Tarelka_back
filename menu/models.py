from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50, blank=False)
    amount = models.IntegerField(blank=True)
    unit = models.CharField(max_length=50, blank=True)
    dish_id = models.ForeignKey('Dish', related_name='ingredients_list', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']


class Dish(models.Model):
    name = models.CharField(max_length=300, blank=False)
    recipe = models.TextField()
    kitchen = models.CharField(max_length=300, blank=True)
    diet = models.CharField(max_length=300, blank=True)
    calories = models.IntegerField(blank=True)
    carbs = models.IntegerField(blank=True)
    fats = models.IntegerField(blank=True)
    proteins = models.IntegerField(blank=True)
    timeOfCooking = models.IntegerField(blank=True)

    class Meta:
        ordering = ['name']


    #picture by url?
