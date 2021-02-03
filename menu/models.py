from django.db import models

CUISINES = (('RU', "РУССКАЯ"), ('B', "ЛУЧШАЯ"), ('P', "ПЕНДОССКАЯ"))
DIETS = (('BP', "БОДИПОЗИТИВ"), ('FN', "ФИТОНЯШКА"), ('NCH', "НОРМ ЧЕЛИК"))
MEAL_TIME = (('B', 'Завтрак'), ('L', 'Обед'), ('D', 'Ужин'),
    ('BL', 'Завтрак и Обед'), ('BD', 'Завтрак и Ужин'), ('LD', 'Обед и Ужин'),
    ('BLD', 'Любое'))

class Preference(models.Model):
    cuisine = models.CharField(choices=CUISINES, default='P', max_length=50)
    diet = models.CharField(choices=DIETS, default='NCH', max_length=50)

    def __str__(self):
        return self.cuisine + ' ' + self.diet

    class Meta:
        ordering=['id']



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
    calories = models.IntegerField(blank=True)
    carbs = models.IntegerField(blank=True)
    fats = models.IntegerField(blank=True)
    proteins = models.IntegerField(blank=True)
    timeOfCooking = models.IntegerField(blank=True)

    mealTime = models.CharField(choices=MEAL_TIME, default='BLD', max_length=100)
    preferenceType = models.ForeignKey('Preference', related_name='dishes',
        blank=True, null=True, on_delete=models.DO_NOTHING)


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
