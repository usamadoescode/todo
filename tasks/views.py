from datetime import timedelta
from django.shortcuts import render , redirect
from .models import Add_task # type: ignore


def create_task (request):
    if request.method == "POST":
        data= request.POST
        task_name= data.get('task_description')
        task_category= data.get('task_category')
        duration=data.get('duration')
        status=data.get('status')

        try:
            # Parse duration as hours or minutes (e.g., '2:30' -> 2 hours, 30 mins)
            hours, minutes = map(int, duration.split(':'))
            duration = timedelta(hours=hours, minutes=minutes)
        except (ValueError, AttributeError):
            duration = timedelta()  
            # Default to 0 if parsing fails
        Add_task.objects.create(
            task_name=task_name,
            task_category=task_category,
            duration=duration,
            status=status,
        )
        return redirect('all_task')
    return render(request, 'tasks/create_task.html')

def all_task(request):

    tasks= Add_task.objects.all() #We are retreiving all data in the DB of tasks
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def delete_task(request,id):
    tasks= Add_task.objects.get(id=id)
    tasks.delete()
    return redirect('all_task')
# Assuming Add_task is the correct model

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
