
from django.urls import path, include

urlpatterns = [
    path('', include('recipes.urls')),
    path('users', include('users.urls')),
]
