from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    mobile = models.IntegerField()


