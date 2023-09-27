"""NotesSharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('login',user_login,name='login'),
    path('admin_home',admin_home,name='admin_home'),
    path('admin_login',admin_login,name='admin_login'),
    path('logout',Logout,name='logout'),
    path('user_profile',user_profile,name='user_profile'),
    path('signup',user_signup,name='signup'),
    path('changepassword',changepassword,name='changepassword'),
    path('editprofile',editprofile,name='editprofile'),
    path('upload_notes',upload_notes,name='upload_notes'),
    path('view_notes',view_notes,name='view_notes'),
    path('delete_mynotes/<int:pid>',delete_mynotes,name='delete_mynotes'),
    path('view_users',view_users,name='view_users'),
    path('delete_users/<int:pid>',delete_users,name='delete_users'),
    path('pending_notes',pending_notes,name='pending_notes'),
    path('accepted_notes',accepted_notes,name='accepted_notes'),
    path('rejected_notes',rejected_notes,name='rejected_notes'),
    path('all_notes',all_notes,name='all_notes'),
    path('assign_status/<int:pid>',assign_status,name='assign_status'),
    path('delete_notes/<int:pid>',delete_notes,name='delete_notes'),
    path('view_allnotes',view_allnotes,name='view_allnotes'),

    path('',index,name='index')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
