from django import forms
from .models import Add_task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_task(forms.ModelForm):
    class Meta:
        model = Add_task
        fields= ['task_name','task_category','duration','status','created_on']

