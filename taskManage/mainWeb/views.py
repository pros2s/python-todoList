from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'mainWeb/Index.html', {
        'title': 'Главная страница'
    })


def taskList(request):
    tasks = Task.objects.order_by('-id')[:7]
    return render(request, 'mainWeb/taskList.html', {
        'title': 'Список заданий',
        'tasks': tasks
    })


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskList')
        else:
            error = 'Неверные данные'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainWeb/create.html', context)