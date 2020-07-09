from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request,'index.html',context)

def details(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    context = {
        'todo':todo
    }
    return render(request,'details.html',context)

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        todo = Todo(title=title, text=text)
        todo.save()
        #return render('/todos',{msg:'Article Added'})
        return redirect('/todos')
    else:
        return render(request,'add.html')