import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Add_task(models.Model):
    Status_choice = [
        ('Done', 'done'),
        ('Pending', 'pending')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Link tasks to users

    task_name = models.CharField(max_length=255, blank=False, null=False)
    task_category = models.CharField(max_length=255, blank=False, null=False)
    duration = models.DurationField()
    status = models.CharField(max_length=10, choices=Status_choice, default='Pending')
    created_on = models.DateTimeField(default=timezone.now)  # Manually set default
    session_id = models.CharField(max_length=100, blank=True, null=True)  # 🔹 Add this field

    def __str__(self):
        return f"{self.task_name}  ({self.status})"
