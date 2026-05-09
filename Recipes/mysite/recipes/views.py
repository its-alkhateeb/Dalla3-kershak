from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Recipe
from django.contrib.auth.decorators import login_required



def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ListOfRecipes.html', {'recipes': recipes})


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



# ==============Add Recipes============
@login_required
def add_recipe(request):

    if request.method == "POST":

        name = request.POST.get("name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        calories = request.POST.get("calories")
        serves = request.POST.get("serves")
        prep_time = request.POST.get("prep_time")

        ingredients = request.POST.getlist("ingredients")
        instructions = request.POST.getlist("instructions")

        image = request.FILES.get("image")

        Recipe.objects.create(
            name=name,
            category=category,
            description=description,
            calories=calories,
            serves=serves,
            prep_time=prep_time,
            ingredients="\n".join(ingredients),
            instructions="\n".join(instructions),
            image=image
        )

        return redirect("home")

    return render(request, "addPage.html")



# ==============Edit Recipes============

@login_required
def edit_recipe(request, pk):

    recipe = get_object_or_404(Recipe, pk=pk)

    # display only
    ingredients_list = [i for i in recipe.ingredients.splitlines() if i.strip()]
    instructions_list = [i for i in recipe.instructions.splitlines() if i.strip()]

    if request.method == 'POST':

        name         = request.POST.get('name', '').strip()
        category     = request.POST.get('category', '').strip()
        description  = request.POST.get('description', '').strip()
        calories     = request.POST.get('calories', '').strip()
        serves       = request.POST.get('serves', '').strip()
        prep_time    = request.POST.get('prep_time', '').strip()

        ingredients  = request.POST.getlist('ingredients')
        instructions = request.POST.getlist('instructions')

        if not name or not category:
            return render(request, 'editRecipe.html', {
                'recipe': recipe,
                'ingredients': ingredients_list,
                'instructions': instructions_list,
                'error': 'Name and category are required.'
            })

        recipe.name        = name
        recipe.category    = category
        recipe.description = description
        recipe.calories    = calories
        recipe.serves      = serves
        recipe.prep_time   = prep_time

        recipe.ingredients = "\n".join([i.strip() for i in ingredients if i.strip()])
        recipe.instructions = "\n".join([i.strip() for i in instructions if i.strip()])

        if request.FILES.get('image'):
            recipe.image = request.FILES.get('image')

        recipe.save()

        return redirect('recipe_detail', pk=recipe.pk)

    return render(request, 'editRecipe.html', {
        'recipe': recipe,
        'ingredients': ingredients_list,
        'instructions': instructions_list,
    })
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients_list = recipe.ingredients.split('\n')
    instructions_list = recipe.instructions.split('\n')
    context = {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
        'instructions_list': instructions_list
    }
    return render(request, 'recipe_detail.html', context)



# ==============Delete Recipes============
@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')
