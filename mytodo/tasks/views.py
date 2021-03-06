from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo
from django.shortcuts import render

# Create your views here.
# noch ein Kommentar
#nochmal ein Kommentar


def index(request):
    latest_todo_list = Todo.objects.order_by('id')[:20]
    parst_date_list = []
    for todo in latest_todo_list:
        todo.deadline = todo.deadline.date()
        parst_date_list = parst_date_list + [todo]
    context = {'latest_todo_list': parst_date_list}
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
    context = {}
    return render(request, 'tasks/save.html', context)


def loeschen(request):
    todos = Todo.objects.all()
    for o in todos:
        if str(o.id) in request.POST:
            o.delete()
    latest_todo_list = Todo.objects.order_by('id')[:1000]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'tasks/loeschen.html', context)


def bearbeiten(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.deadline.month < 10 and todo.deadline.day < 10:
        newdate = str(todo.deadline.year) + "-" + "0" +str(todo.deadline.month) + "-" + "0" + str(todo.deadline.day)
    elif todo.deadline.month < 10:
        newdate = str(todo.deadline.year) + "-" + "0" + str(todo.deadline.month) + "-" + str(todo.deadline.day)
    elif todo.deadline.day < 10:
        newdate = str(todo.deadline.year) + "-" + str(todo.deadline.month) + "-" + "0" + str(todo.deadline.day)
    else:
        newdate = str(todo.deadline.year) + "-" + str(todo.deadline.month) + "-" + str(todo.deadline.day)
    print(newdate)
    context = {'todo': todo, 'date': newdate}
    return render(request, 'tasks/bearbeiten.html', context)


def save(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.description = request.POST['descriptiontask']
    todo.deadline = request.POST['deadline']
    todo.done = request.POST['done']
    todo.save()
    context = {}
    return render(request, 'tasks/save.html', context)

def beispiel(request):
    context = {}
    return render(request, 'tasks/beispiel.html', context)


def impressum(request):
    context = {}
    return render(request, 'tasks/impressum.html', context)

