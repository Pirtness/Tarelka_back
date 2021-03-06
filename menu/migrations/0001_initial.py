# Generated by Django 3.1.5 on 2021-02-03 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('recipe', models.TextField()),
                ('calories', models.IntegerField(blank=True)),
                ('carbs', models.IntegerField(blank=True)),
                ('fats', models.IntegerField(blank=True)),
                ('proteins', models.IntegerField(blank=True)),
                ('timeOfCooking', models.IntegerField(blank=True)),
                ('mealTime', models.CharField(choices=[('B', 'Завтрак'), ('L', 'Обед'), ('D', 'Ужин'), ('BL', 'Завтрак и Обед'), ('BD', 'Завтрак и Ужин'), ('LD', 'Обед и Ужин'), ('BLD', 'Любое')], default='BLD', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(choices=[('RU', 'РУССКАЯ'), ('B', 'ЛУЧШАЯ'), ('P', 'ПЕНДОССКАЯ')], default='P', max_length=50)),
                ('diet', models.CharField(choices=[('BP', 'БОДИПОЗИТИВ'), ('FN', 'ФИТОНЯШКА'), ('NCH', 'НОРМ ЧЕЛИК')], default='NCH', max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WeekMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(blank=True)),
                ('endDate', models.DateField(blank=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekMenus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField(blank=True)),
                ('unit', models.CharField(blank=True, max_length=50)),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_list', to='menu.dish')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='preferenceType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dishes', to='menu.preference'),
        ),
        migrations.CreateModel(
            name='DayMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(blank=True)),
                ('breakfast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breakfasts', to='menu.dish')),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinners', to='menu.dish')),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lunches', to='menu.dish')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayMenus', to='menu.weekmenu')),
            ],
        ),
    ]
