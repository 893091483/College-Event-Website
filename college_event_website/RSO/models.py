from django.db import models
from Users.models import User
from Universities.models import University
from django.db.models import ManyToManyField

# Create your models here.
class Rso(models.Model):
  id = models.AutoField(primary_key=True) 
  name = models.CharField(max_length = 255, null=False)
  # students = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')
  university =  models.ForeignKey(University, on_delete=models.CASCADE, related_name='University', null=True)
  students = ManyToManyField(User)
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin', null=True)

  def __str__(self):
    return self.name