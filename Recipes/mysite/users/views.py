from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    return render(request, 'Sign up.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

