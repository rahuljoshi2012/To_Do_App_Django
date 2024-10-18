from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todolist import models
from todolist.models import todo
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        obj = User.objects.create_user(Username, Email, Password)
        obj.save()
        return redirect('loginn')
    return render(request, "signup.html")

def loginn(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def todolis(request):
    if request.method == "POST":
        if 'title' in request.POST:
            title = request.POST.get('title')
            obj1 = todo(title=title, user=request.user)
            obj1.save()
        elif 'task_id' in request.POST:
            task_id = request.POST.get('task_id')
            if task_id:
                todo.objects.filter(srno=task_id, user=request.user).delete()
        return redirect('todo')
    
    tasks = todo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'tasks': tasks})
