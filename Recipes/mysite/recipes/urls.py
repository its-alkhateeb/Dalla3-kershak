from django.urls import path
from .views import recipes_list
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', views.recipes_list, name='recipes_list'),
    path('profile/', views.profile, name='profile'),
    path('favourites/', views.favourites, name='favorites'),
]