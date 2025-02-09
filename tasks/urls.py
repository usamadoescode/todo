from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   
    path('', views.all_task, name='all_task'),  # All tasks
    path('create_task/', views.create_task, name='create_task'), 
    path('delete-Add_task/<id>/', views.delete_task, name='delete_task'), 
    path('update-Add_task/<id>/', views.update_task, name='update_task'), 






      # Create task with trailing slash
]
