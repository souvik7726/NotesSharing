from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def user_login(request):
    error=""
    if request.method == 'POST':
        u=request.POST['eml']
        p=request.POST['pass']
        user= authenticate(username=u, password=p)
        try:
            if user:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error': error}
    return render(request,'login.html', d)
def admin_login(request):
    error=""
    if request.method == 'POST':
        u=request.POST['uname']
        p=request.POST['pass']
        user= authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error': error}
    return render(request,'admin_login.html', d)
def user_signup(request):
    error=""
    if request.method=='POST':
        f=request.POST['fnm']
        l=request.POST['lnm']
        e=request.POST['emailid']
        p=request.POST['phn']
        br=request.POST['branch']
        rol=request.POST['pos']
        pwd=request.POST['pass']
        try:
            user=User.objects.create_user(username=e,password=pwd,first_name=f,last_name=l)
            signup.objects.create(user=user,contact=p,branch=br,role=rol)
            error="no"
        except:
            error="yes"

    d={'error':error}
    return render(request,'signup.html',d)
def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    return render(request,'admin_home.html')
def Logout(request):
    logout(request)
    return redirect('index')
def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=signup.objects.get(user=user)
    d={'data':data,'user':user}
    return render(request,'profile.html',d)
