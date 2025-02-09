from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect("login")  # Redirects to login page if user visits "/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_login, name="home"),  # Default to login page
    path("accounts/", include("accounts.urls")),  # Includes your accounts app URLs
]
