from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.


def newtodo(request):
    return render(request, 'tasks/newtodo.html')


def savenewtodo(request):
    description = request.POST['descriptiontask']
    deadline = request.POST['deadline']
    todo = Todo.objects.create(
        description=description,
        deadline=deadline
    )
    return HttpResponse("Speichern war erfolgreich.")

