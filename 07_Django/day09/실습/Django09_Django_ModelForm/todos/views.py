from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            context = {
                'form': form
            }
            return redirect('todos:index')

    else:
        form = TodoForm()

    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)  # 확인 필요
    todo.delete()
    return redirect('todos:index')

# # delete에서 post 사용방법(?) -@ 데코레이터 POST인 경우에만 실행
# @require_POST
# def delete(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     if request.method == 'POST':
#         todo.delete()
#         return redirect('todos:index')


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        # instance=todo 객체를 명시해줌
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)

    context = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'todos/update.html', context)
