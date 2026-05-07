from django.shortcuts import render



from django.http import JsonResponse
from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    data = list(recipes.values())
    return JsonResponse(data, safe=False)


def home(request):
    return render(request, 'Home.html')

def favourites(request):
    return render(request, 'Favourites.html')



# def recipes_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'ListOfRecipes.html', {
#         'recipes': recipes
#     })

def profile(request):
    return render(request, 'profile.html')