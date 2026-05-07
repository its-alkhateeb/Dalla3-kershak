from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    calories = models.CharField(max_length=50, blank=True, null=True)
    serves = models.CharField(max_length=50, blank=True, null=True)
    prep_time = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    favorites = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)
    image = models.ImageField(default='default_recipe.jpg', upload_to='recipe_pics')

    def __str__(self):
        return self.name
