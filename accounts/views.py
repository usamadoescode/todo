from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from tasks.models import Add_task  # ✅ Import your task model

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("tasks:all_task")  # ✅ Redirect to the user's tasks
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect("tasks:all_task")  # ✅ Redirect logged-in users to their tasks
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tasks:all_task")  # ✅ Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("accounts:user_login")  # ✅ Redirect to login after logout
