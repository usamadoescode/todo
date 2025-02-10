from django.urls import path
from . import views

app_name = "tasks"  # ✅ Namespace is required

urlpatterns = [
    path("", views.all_task, name="all_task"),  # ✅ This must be named correctly
    path("create_task/", views.create_task, name="create_task"),
    path("delete_task/<int:id>/", views.delete_task, name="delete_task"),
    path("update_task/<int:id>/", views.update_task, name="update_task"),
]
