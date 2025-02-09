from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # ✅ Default URL now loads `accounts/urls.py`, which shows login by default
    path("", include("accounts.urls")),  

    path("tasks/", include("tasks.urls")),  
]
