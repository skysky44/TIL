from django.shortcuts import render
from .models import Todo
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    print(todo)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    # print(request.GET)
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    todo = Todo(title=title, content=content,
                priority=priority, deadline=deadline)
    todo.save()
    return render(request, 'todos/create.html')
