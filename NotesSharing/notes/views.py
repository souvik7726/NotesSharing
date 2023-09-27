from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
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
    pend=Notes.objects.filter(status="pending").count()
    acc=Notes.objects.filter(status="accept").count()
    rej=Notes.objects.filter(status="reject").count()
    all=Notes.objects.all().count()
    d={'pend':pend,'acc':acc,'rej':rej,'all':all}
    return render(request,'admin_home.html',d)




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
def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=signup.objects.get(user=user)
    error=""
    if request.method=='POST':
        f=request.POST['fnm']
        l=request.POST['lnm']
        c=request.POST['contact']
        br=request.POST['branch']
        user.first_name=f
        user.last_name=l
        data.contact=c
        data.branch=br
        user.save()
        data.save()
        error="no"
    

    d={'data':data,'user':user, 'error':error}
    return render(request,'editprofile.html',d)

def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=="POST":
        oldpwd=request.POST['old']
        newpwd=request.POST['new']
        cfmpwd=request.POST['confirm']

        if newpwd==cfmpwd:
            u=User.objects.get(username__exact=request.user.username)
            u.set_password(newpwd)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'changepassword.html',d)


def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        b=request.POST['branch']
        s=request.POST['subject']
        n=request.FILES['notesfile']
        f=request.POST['filetype']
        d=request.POST['description']
        u=User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=d,status='pending')
            error="no"
        except:
            error="yes"

    d={'error':error}
    return render(request,'upload_notes.html',d)

def view_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    notes=Notes.objects.filter(user=user)

    d={'notes':notes}
    return render(request,'view_notes.html',d)

def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_notes')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    users=signup.objects.all()
    d={'users':users}
    return render(request,'view_users.html',d)

def delete_users(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

def pending_notes(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notes=Notes.objects.filter(status="pending")
    d={'notes':notes}
    return render(request,'pending_notes.html',d)

def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notes=Notes.objects.filter(status="accept")
    d={'notes':notes}
    return render(request,'accepted_notes.html',d)

def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notes=Notes.objects.filter(status="reject")
    d={'notes':notes}
    return render(request,'rejected_notes.html',d)

def all_notes(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notes=Notes.objects.all()
    d={'notes':notes}
    return render(request,'all_notes.html',d)

def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notes=Notes.objects.get(id=pid)
    error=""
    if request.method=='POST':
        s=request.POST['status']
        try:
            notes.status=s
            notes.save()
            error="no"
        except:
            error="yes"
    d={'notes':notes,'error':error}
    return render(request,'assign_status.html',d)

def delete_notes(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('all_notes')

def view_allnotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    notes=Notes.objects.filter(status="accept")
    d={'notes':notes}
    return render(request,'view_allNotes.html',d)