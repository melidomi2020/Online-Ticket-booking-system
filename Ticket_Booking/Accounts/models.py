""" from django.db import models
from django.contrib.auth.models import User
from .managers import PersonManager

class Student(User):
    objects = PersonManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )  """

    #def do_something(self)
# Create your models here.
