from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if(request.method=='POST'):
        fm=StudentRegistration(request.POST)
        if(fm.is_valid()):
            nm1=fm.cleaned_data['first_name']
            nm2=fm.cleaned_data['last_name']
            em=fm.cleaned_data['email']
            uid=fm.cleaned_data['uniqueid']
            pwd=fm.cleaned_data['password']
            rpwd=fm.cleaned_data['rpassword']
            reg=User(first_name=nm1,last_name=nm2,email=em,uniqueid=uid)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'addandshow.html',{'form':fm,'stu':stud})

def Delete(request,id):
    if(request.method=='POST'):
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def Update(request,id):
    if(request.method=='POST'):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST)
        if(fm.is_valid()):
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'update_data.html',{'form':fm})

def Login(request,id):
    if(request.method=='POST'):
        fm=StudentRegistration(request.POST)
        if(fm.is_valid()):
            em1=fm.cleaned_data['email']
            pwd1=fm.cleaned_data['password']
            reg=User(email=em1,password=pwd1)
            reg.save()
    else:
        StudentRegistration()

    return render(request,'login.html',{'fm':fm})

    


        
