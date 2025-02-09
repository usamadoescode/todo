from datetime import timedelta
from django.shortcuts import render, redirect
from .models import Add_task  # type: ignore
from django.contrib.auth.decorators import login_required

@login_required
def create_task(request):
    # Ensure the session exists
    if not request.session.session_key:
        request.session.create()  

    session_id = request.session.session_key  

    if request.method == "POST":
        data = request.POST
        task_name = data.get('task_name')
        task_category = data.get('task_category')
        duration = data.get('duration')
        status = data.get('status')

        # Convert duration string (e.g., "2:30") into a timedelta object
        try:
            hours, minutes = map(int, duration.split(':'))
            duration = timedelta(hours=hours, minutes=minutes)
        except (ValueError, AttributeError):
            duration = timedelta()

        # Save task with session_id
        Add_task.objects.create(
            task_name=task_name,
            task_category=task_category,
            duration=duration,
            status=status,
            session_id=session_id  # Link task to session
        )

        return redirect("tasks:all_task")  # ✅ Correct

    return render(request, 'tasks/create_task.html')

@login_required
def all_task(request):
    if not request.session.session_key:
        request.session.create()

    session_id = request.session.session_key
    tasks = Add_task.objects.filter(session_id=session_id)

    return render(request, 'tasks/tasks.html', {'tasks': tasks})

from django.shortcuts import get_object_or_404

@login_required
def delete_task(request, id):
    task = get_object_or_404(Add_task, id=id)
    task.delete()
    return redirect('tasks:all_task')
# Assuming Add_task is the correct model
@login_required
def update_task(request, id):
    task = get_object_or_404(Add_task, id=id)

    if request.method == "POST":
        task.task_name = request.POST.get('task_name')
        task.task_category = request.POST.get('task_category')

        duration = request.POST.get('duration')
        try:
            hours, minutes = map(int, duration.split(':'))
            task.duration = timedelta(hours=hours, minutes=minutes)
        except (ValueError, AttributeError):
            task.duration = timedelta()  

        task.status = request.POST.get('status')
        task.save()

        return redirect('tasks:all_task')

    return render(request, 'tasks/update_task.html', {'tasks': task})

