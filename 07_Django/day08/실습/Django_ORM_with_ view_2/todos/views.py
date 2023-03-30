from django.shortcuts import render, redirect
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
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    todo = Todo()
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')
    todo.save()

    return redirect('todos:index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/edit.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')
    todo.save()

    return redirect('todos:index')


def completed(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:index')
