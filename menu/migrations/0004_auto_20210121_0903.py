# Generated by Django 3.1.5 on 2021-01-21 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_daymenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='daymenu',
            name='breakfast',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='breakfasts', to='menu.dish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daymenu',
            name='dinner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dinners', to='menu.dish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daymenu',
            name='lunch',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='lunches', to='menu.dish'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daymenu',
            name='day',
            field=models.DateField(blank=True),
        ),
    ]
