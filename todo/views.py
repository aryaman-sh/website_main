from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import templates
from . import models
from .forms import CreateTodo, UpdateTodo

app_name = "todo"


@login_required(login_url="/accounts/login")
def test(request):
    return render(request, 'todo/all_todo.html')


@login_required(login_url="/accounts/login")
def index(request):
    items = models.TodoItem.objects.all().filter(author=request.user).order_by('created')
    return render(request, 'todo/all_todo.html', {'items': items})


@login_required(login_url="/accounts/login")
def add_todo(request):
    if request.method == "GET":
        form = CreateTodo()
    else:
        form = CreateTodo(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('todo:index')
    return render(request, 'todo/add_todo.html', {'form': form})


@login_required(login_url="/accounts/login")
def delete(request, del_id):
    obj = models.TodoItem.objects.get(id=del_id)
    obj.delete()
    return redirect('todo:index')


@login_required(login_url="/accounts/login")
def update(request, update_id):
    if request.method == "GET":
        obj = get_object_or_404(models.TodoItem, id=update_id)
        form = UpdateTodo(initial={'item': obj.item, 'created':obj.created, 'due':obj.due})
    else:
        obj = get_object_or_404(models.TodoItem, id=update_id)
        form = UpdateTodo(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    return render(request, 'todo/update_todo.html', {'form': form, 'obj': obj})
