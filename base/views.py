from django.shortcuts import render,redirect
from .models import TaskModel,CompletedModel,TrashModel


# Create your views here.
def home(request):
    data=TaskModel.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method=='POST':
        title_data=request.POST['title']
        des_data=request.POST['des']
        TaskModel.objects.create(
            title=title_data,
            des=des_data

        )
        return redirect(home)
    return render(request,'add.html')


def completed(request):
    data=CompletedModel.objects.all()
    return render(request,'completed.html',{'data':data})

def trash(request):
     data=TrashModel.objects.all()
     return render(request,'trash.html',{'data':data})

def about(request):
     return render(request,'about.html')

def update(request,pk):
    data=TaskModel.objects.get(id=pk)
    if request.method=='POST':
        title_data=request.POST['title']
        des_data=request.POST['des']
        data.title=title_data
        data.des=des_data
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})


def hcompleted(request,pk):
    data=TaskModel.objects.get(id=pk)
    CompletedModel.objects.create(
        title=data.title,
        des=data.des
    )
    data.delete()
    return redirect('home')

def hdelete(request,pk):
    data=TaskModel.objects.get(id=pk)
    TrashModel.objects.create(
        title=data.title,
        des=data.des
    )
    data.delete()
    return redirect('home')


def hcompletedall(request):
    data=TaskModel.objects.all()
    for i in data:
        CompletedModel.objects.create(
            title=i.title,
            des=i.des
        )
        i.delete()
    
    return redirect('home')

def deleteall(request):
    data=TaskModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title=i.title,
            des=i.des
        )
        i.delete()
    
    return redirect('home')

def delete(request,pk):
    a=TrashModel.objects.get(id=pk)
    a.delete()
    return redirect('trash')




def cdeleteall(request):
    data=CompletedModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title=i.title,
            des=i.des
        )
        i.delete()
    
    return redirect('trash')

def cdelete(request,pk):
    a=CompletedModel.objects.get(id=pk)
    a.delete()
    return redirect('trash')

def crestore(request,pk):
    data=CompletedModel.objects.get(id=pk)
    TaskModel.objects.create(
            title=data.title,
            des=data.des
        )
    data.delete()
    return redirect('completed')

def crestoreall(request):
    data=CompletedModel.objects.all()
    for i in data:
        TaskModel.objects.create(
            title=i.title,
            des=i.des
        )
        i.delete()
    
    return redirect('completed')


def tdeleteall(request):
    data=TrashModel.objects.all()
    data.delete()
    return redirect('trash')


def trestore(request,pk):
    data=TrashModel.objects.get(id=pk)
    TaskModel.objects.create(
            title=data.title,
            des=data.des
        )
    data.delete()
    return redirect('trash')

def trestoreall(request):
    data=TrashModel.objects.all()
    for i in data:
        TaskModel.objects.create(
            title=i.title,
            des=i.des
        )
        i.delete()
    
    return redirect('trash')