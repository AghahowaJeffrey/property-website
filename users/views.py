from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomLoginForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'].lower()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match.')

    return redirect('home')



def custom_login_view(request):
    """
    A custom login view to handle login requests manually.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect("dashboard")  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password.")
    
    return redirect("home")
