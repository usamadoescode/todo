from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import Add_task
from django.contrib.auth.decorators import login_required

@login_required
def create_task(request):
    if request.method == "POST":
        data = request.POST
        task_name = data.get('task_name')
        task_category = data.get('task_category')
        status = data.get('status')

        # Save task with the logged-in user
        Add_task.objects.create(
            task_name=task_name,
            task_category=task_category,
            status=status,
            user=request.user  # ✅ Link task to user
        )

        return redirect("tasks:all_task")  # ✅ Redirect after creation

    return render(request, 'tasks/create_task.html')

@login_required
def all_task(request):
    tasks = Add_task.objects.filter(user=request.user)  # ✅ Fetch tasks for the logged-in user only
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Add_task, id=id, user=request.user)  # ✅ Ensure user can only delete their own tasks
    task.delete()
    return redirect('tasks:all_task')

@login_required
def update_task(request, id):
    task = get_object_or_404(Add_task, id=id, user=request.user)  # ✅ Ensure user can only update their own tasks

    if request.method == "POST":
        task.task_name = request.POST.get('task_name')
        task.task_category = request.POST.get('task_category')
        task.status = request.POST.get('status')
        task.save()

        return redirect('tasks:all_task')

    return render(request, 'tasks/update_task.html', {'task': task})
