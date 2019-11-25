from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from testapp.forms import userform

@login_required()
def listemp(request):
        uname=request.user.username
        print(uname,"unameeeeeeeeeeeeeeeeeeeeeeeee")
        obj = User.objects.get(username=request.user.username)
        return render(request,'testapp/list.html',{"obj":obj})


def signupform(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})