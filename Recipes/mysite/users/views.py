from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        # Manually inject is_admin as bool since it comes as a string from hidden input
        post_data = request.POST.copy()
        post_data['is_admin'] = post_data.get('is_admin') == 'true'

        form = RegisterForm(post_data, request.FILES)
        if form.is_valid():
            image = request.FILES.get('profile_picture')
            user = form.save()
            if image:
                user.profile.image = image
                user.profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'Signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not found. Please sign up first.")
            return redirect('signup')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next')
            return redirect(next_page if next_page else 'home')
        else:
            return render(request, 'login.html', {
                'error_message': 'Invalid username or password. Please try again.'
            })
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def dashboard(request):
    return render(request, 'dashboard.html')