from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo
from django.shortcuts import render

# Create your views here.


def index(request):
    latest_todo_list = Todo.objects.order_by('id')[:20]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'tasks/index.html', context)


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


def loeschen(request):
    todos = Todo.objects.all()
    for o in todos:
        if str(o.id) in request.POST:
            o.delete()
    latest_todo_list = Todo.objects.order_by('id')[:20]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'tasks/loeschen.html', context)

