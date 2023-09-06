from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact=models.CharField(max_length=10,null=True)
    branch=models.CharField(max_length=30,null=True)
    role=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate=models.CharField(max_length=10,null=True)
    branch=models.CharField(max_length=30)
    subject=models.CharField(max_length=20)
    notesfile=models.FileField(null=True)
    filetype=models.CharField(max_length=20, null=True)
    description=models.CharField(max_length=400,null=True)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.signup.user.username+" "+self.status
    
    
    

