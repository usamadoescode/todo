from django.urls import path
from . import views
app_name = "tasks"
urlpatterns = [
    
    path("", views.user_login, name="user_login"),  # ✅ Default page is login
    path("register/", views.register, name="register"),
    path("logout/", views.user_logout, name="logout"),
]
