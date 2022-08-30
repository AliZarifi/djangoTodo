from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .form import TodoForm
from .models import Todo

# Create your views here.
def signupuser(request):
    if request.method=='GET':
        return render(request,'todoapp/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            user.save()
        else:
            return render(request,'todoapp/signupuser.html',{'form':UserCreationForm(),'error':'pass didnot matche'})


    
def create(request):
    if request.method=='GET':
        return render(request,'todoapp/create.html',{'form':TodoForm()})
    else:
        try:
            form =TodoForm(request.POST)
            newtodo=form.save(commit=False)
            newtodo.user=request.user
            newtodo.save()
            return redirect('currenttodo')
        except:
            return render(request,'todoapp/create.html',{'form':TodoForm()})


def current(request):
    todo=Todo.objects.all()
    return render(request,'todoapp/todolist.html',{'todos':todo})

