# Generated by Django 3.1.5 on 2021-01-25 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210125_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='daymenu',
            name='menu_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dayMenus', to='menu.weekmenu'),
            preserve_default=False,
        ),
    ]