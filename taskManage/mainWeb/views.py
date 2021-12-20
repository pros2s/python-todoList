from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')[:4]
    return render(request, 'mainWeb/index.html', {
        'title': 'Главная страница',
        'tasks': tasks
    })


def about(request):
    return render(request, 'mainWeb/about.html', {
        'title': 'О нас'
    })


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверные данные'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainWeb/create.html', context)