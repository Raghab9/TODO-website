from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'home.html',{'data':data})


def add(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        TaskModel.objects.create(
            title=title,
            desc=desc
        )
        return redirect('home')
    return render(request,'add.html')

def update(request,pk):
    data=TaskModel.objects.get(id=pk)
    
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        data.title=title
        data.desc=desc
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})

def complete(request):
    a=CompleteModel.objects.all()
    return render(request,'complete.html',{'data':a})

def complete_(request,pk):
    a=TaskModel.objects.get(id=pk)
    CompleteModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('home')


def trash(request):
    a=TrashModel.objects.all()
    return render(request,'trash.html',{'data':a})

def about(request):
    return render(request,'about.html')

def delete(request,pk):
    a = TaskModel.objects.get(id=pk) #fletch the reccord from the databse

    TrashModel.objects.create(
        title=a.title,
        desc=a.desc
    )#create the record in the trash databse

    a.delete()#delete the the record taskmodel
    return redirect('home')

def delete_all(request):
    a=TaskModel.objects.all()
    for i in a:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('home')  

def complete_all(request):
    a=TaskModel.objects.all()
    for i in a:
        CompleteModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('complete')    

def complete_deleteAll(request):
    a=CompleteModel.objects.all()
    for i in a:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('complete')

def crstoreall(request):
    a=CompleteModel.objects.all()
    for i in a:
        TaskModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('home')


def crestore(request,pk):
    a=CompleteModel.objects.get(id=pk)
    TaskModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('complete')



def cdelete(request,pk):
    a=CompleteModel.objects.get(id=pk)
    TrashModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('complete')

def trestore(request,pk):
    a=TrashModel.objects.get(id=pk)
    TaskModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('home')


def tdelete(request,pk):
    a=TrashModel.objects.get(id=pk)
    a.delete()
    return redirect('trash')

def trestoreall(request):
    a=TrashModel.objects.all()
    for i in a:
        TaskModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('home')

def tdeleteall(request):
    a=TrashModel.objects.all()
    a.delete()
    return redirect('home')


#on the home page create complete all button
#complete mai delete button and dellete all
#delete all in trash