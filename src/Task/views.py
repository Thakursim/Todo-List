from django.shortcuts import render
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
    # redirect the browser to "/"
    
def delete_task(request, task_id):
    a = Task.objects.get(id=task_id)
    a.delete()
    return HttpResponseRedirect('/todo/')