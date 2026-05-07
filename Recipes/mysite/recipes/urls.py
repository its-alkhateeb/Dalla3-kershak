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
]