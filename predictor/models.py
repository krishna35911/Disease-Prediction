from django.db import models

class reg(models.Model):
    name=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    add=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    psw=models.CharField(max_length=200,null=True)
class doctor(models.Model):
    name=models.CharField(max_length=200,null=True)
    hos=models.CharField(max_length=200,null=True)
    spcl=models.CharField(max_length=200,null=True)
    place=models.CharField(max_length=200,null=True)
    mobile=models.CharField(max_length=200,null=True)    
    

class resmodel(models.Model):
    name=models.CharField(max_length=200,null=True)
    disease=models.CharField(max_length=200,null=True)
    
