from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

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

    def average_rating(self):
        result = self.ratings.aggregate(Avg('score'))['score__avg']
        return result if result is not None else 0

    def __str__(self):
        return self.name

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    score = models.IntegerField(default=0)

    class Meta:
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"{self.user.username} rated {self.recipe.name}: {self.score}"
