from django.shortcuts import render,redirect
from testapp.models import student
from testapp.forms import studentmodel
# Create your views here.
def retrive_view(request):
    obj=student.objects.all()
    return render(request,'testapp/student_list.html',{'obj':obj})

def create_view(request):
    form=studentmodel()
    if request.method=='POST':
        form=studentmodel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/student_create.html',{'form':form})

def update_view(request,id):
    student_id=student.objects.get(id=id)
    if request.method=='POST':
        form=studentmodel(request.POST,instance=student_id)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("not validaaaaaaaaaa")
    return render(request,'testapp/update.html',{'id':student_id})

def delete_view(request,id):
    student_id=student.objects.get(id=id)
    student_id.delete()
    return redirect('/')