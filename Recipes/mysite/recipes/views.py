from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Recipe, Rating
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def recipes_list(request):
    query = request.GET.get('q', '').strip()
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) |
            Q(ingredients__icontains=query)
        )

    return render(request, 'ListOfRecipes.html', {
        'recipes': recipes,
        'query': query,
    })

def home(request):
    return render(request, 'Home.html')


@login_required
def favourites(request):
    my_favorites = request.user.favorite_recipes.all()
    return render(request, 'Favourites.html', {'recipes': my_favorites})



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

        return redirect("dashboard")

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

        return redirect('recipe_detail', recipe_id=recipe.pk)

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
    return redirect('dashboard')

@login_required
def view_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    recipes = Recipe.objects.all()
    return render(request, 'dashboard.html', {'recipes': recipes})



# ==========================================
# 1. ADD / REMOVE FAVORITE LOGIC
# ==========================================
@login_required
def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # If the user is already in the favorites list, remove them.
    if request.user in recipe.favorites.all():
        recipe.favorites.remove(request.user)
        is_favorited = False
    # If they aren't in the list, add them.
    else:
        recipe.favorites.add(request.user)
        is_favorited = True

    return JsonResponse({'success': True, 'is_favorited': is_favorited})


 
 
def recipes_list(request):
    query = request.GET.get('q', '')
 
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
    else:
        recipes = Recipe.objects.all()
 
   
    user_ratings = {}
    if request.user.is_authenticated:
        my_ratings = Rating.objects.filter(user=request.user)
        for r in my_ratings:
            user_ratings[r.recipe_id] = r.score
 
    return render(request, 'ListOfRecipes.html', {
        'recipes': recipes,
        'query': query,
        'user_ratings': user_ratings,   
    })
 
 
@login_required
def rate_recipe(request, recipe_id):
    if request.method == "POST":
        score = request.POST.get('score')
        recipe = get_object_or_404(Recipe, id=recipe_id)

        Rating.objects.update_or_create(
            recipe=recipe,
            user=request.user,
            defaults={'score': score}
        )

    return redirect('recipes_list')