from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL ,null=True,blank=True)
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname =models.CharField(max_length=100)
    emp_code =models.CharField(max_length=3)
    mobile =models.CharField(max_length=15)
    position =models.ForeignKey(Position,on_delete=models.CASCADE)