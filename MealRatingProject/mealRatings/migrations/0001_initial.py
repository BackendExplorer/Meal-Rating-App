# Generated by Django 5.1.4 on 2025-04-14 11:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('imageUrl', models.URLField()),
                ('countryOfOrigin', models.CharField(max_length=50)),
                ('typicalMealTime', models.IntegerField(choices=[(1, 'Morning'), (2, 'Afternoon'), (3, 'Evening')])),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MealRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('dateOfRating', models.DateTimeField(default=django.utils.timezone.now)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealRatings.meal')),
            ],
        ),
    ]
