from django.shortcuts import render , redirect


def index(request):
    return render(request, 'whatdoing/index.html')  # Looks for index.html in the templates directory
          