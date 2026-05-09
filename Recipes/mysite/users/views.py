from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm , PasswordChangeForm ,RegisterForm
from django.contrib.auth.models import User


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
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    password_form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_profile':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile')

        elif action == 'change_password':
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                request.user.set_password(password_form.cleaned_data['new_password1'])
                request.user.save()
                update_session_auth_hash(request, request.user)  # keeps user logged in
                messages.success(request, 'Password changed successfully.')
                return redirect('profile')

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
    })