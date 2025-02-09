from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('accounts.urls')),  
     path("tasks/", include("tasks.urls")),  # Tasks App
]
