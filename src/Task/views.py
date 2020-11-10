from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Task

# Create your views here.

def todo_view(request):
    show = Task.objects.all()
    return render(request, "todo.html", {'all_items': show})
    
def add_new(request):
    # a = request.POST['work']
    # new_item = Task(work = a)
    new_item = Task(work = request.POST['work'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    #create a new todo all_items
    #save
    # redirect the browser to "/todo/"
    
def update_view(request, task_id):
    update = Task.objects.get(id=task_id)
    if request.POST:
       a = Task.objects.get(id=task_id)
       a.work = request.POST['work2']
       a.save(update_fields=['work'])
       a.save()
       return HttpResponseRedirect('/todo/')    
    return render(request, 'edit.html', {'x': update})
    
def delete_task(request, task_id):
    a = Task.objects.get(id=task_id)
    a.delete()
    return HttpResponseRedirect('/todo/')