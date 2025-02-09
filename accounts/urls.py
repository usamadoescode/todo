from django.urls import path
from . import views

app_name = "accounts"  # ✅ Fix the namespace

urlpatterns = [
    path("", views.user_login, name="user_login"),  # ✅ Login page
    path("register/", views.register, name="register"),  # ✅ Register page
    path("logout/", views.user_logout, name="logout"),  # ✅ Logout page
]
