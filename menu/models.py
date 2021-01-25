from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50, blank=False)
    amount = models.IntegerField(blank=True)
    unit = models.CharField(max_length=50, blank=True)
    dish_id = models.ForeignKey('Dish', related_name='ingredients_list', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    #picture by url?

class WeekMenu(models.Model):
    username = models.ForeignKey('auth.User', related_name='weekMenus', on_delete=models.CASCADE)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)

class DayMenu(models.Model):
    day = models.DateField(blank=True)
    breakfast = models.ForeignKey('Dish', related_name='breakfasts', on_delete=models.CASCADE)
    lunch = models.ForeignKey('Dish', related_name='lunches', on_delete=models.CASCADE)
    dinner = models.ForeignKey('Dish', related_name='dinners', on_delete=models.CASCADE)

    menu_id = models.ForeignKey('WeekMenu', related_name='dayMenus', on_delete=models.CASCADE)


    #def __str__(self):
    #    return self.day
