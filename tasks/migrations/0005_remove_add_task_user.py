# Generated by Django 5.1.3 on 2025-02-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_add_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_task',
            name='user',
        ),
    ]
