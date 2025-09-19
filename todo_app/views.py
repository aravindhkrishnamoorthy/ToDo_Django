from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def homepage(request):
    t = Task.objects.filter(is_completed=False).order_by('updated_at')
    context={'tasks': t,}
    return render(request, "homepage.html", context)

def addtask(request):
    input_task = request.POST['task_addbar']
    Task.objects.create(task=input_task)
    return redirect("homepage")
