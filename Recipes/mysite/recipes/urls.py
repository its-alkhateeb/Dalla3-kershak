from django.urls import path
from .views import recipes_list
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', views.recipes_list, name='recipes_list'),
    path('favourites/', views.favourites, name='favorites'),
    path('recipes/add/', views.add_recipe, name='add_recipe'),
    path('recipes/edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('dashboard/', views.view_dashboard, name='dashboard'),
    path('recipes/<int:recipe_id>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('recipes/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),
]

