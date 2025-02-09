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
        task_name = data.get('task_description')
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
    session_id = request.session.session_key  # Ensure session consistency

    # Retrieve only tasks linked to the current session
    tasks = Add_task.objects.filter(session_id=session_id)

    return render(request, 'tasks/tasks.html', {'tasks': tasks})

@login_required
def delete_task(request,id):
    tasks= Add_task.objects.get(id=id)
    tasks.delete()
    return redirect('all_task')
# Assuming Add_task is the correct model
@login_required

def update_task(request, id):
    try:
        tasks = Add_task.objects.get(id=id)
    except Add_task.DoesNotExist:
        return redirect('all_task')  # If the task doesn't exist, redirect to the task list

    # If the request is a POST (form submission)
    if request.method == "POST":
        # Get the form data
        task_name = request.POST.get('task_description')
        task_category = request.POST.get('task_category')
        duration = request.POST.get('duration')
        status = request.POST.get('status')

        # Handle the duration field (convert string to timedelta)
        try:
            hours, minutes = map(int, duration.split(':'))
            duration = timedelta(hours=hours, minutes=minutes)
        except (ValueError, AttributeError):
            duration = timedelta()  # Default to 0 if parsing fails

        # Update task with the new data
        tasks.task_name = task_name
        tasks.task_category = task_category
        tasks.duration = duration
        tasks.status = status
        tasks.save()  # This will update the existing task in the database

        # Redirect to the task list page after saving
        return redirect('all_task')

    # If it's a GET request (initial load of the form)
    return render(request, 'tasks/update_task.html', {'tasks': tasks})  # Render the template with the task details
