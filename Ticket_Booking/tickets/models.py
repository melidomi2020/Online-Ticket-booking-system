from typing import Counter
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, DateField, DateTimeField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
#from .models import Ticket

# Create your models here.
class Ticket(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,primary_key=False)
    reg_no=models.AutoField(primary_key=True)
    Counter_Choices=(('counter1','counter 1'),('counter2','counter 2'),('counter3','counter 3'),('counter4','counter 4'),('counter5','counter 5'))
    counter=models.CharField(choices=Counter_Choices,max_length=9,default='counter1')
    service=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return str(self.user)