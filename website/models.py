from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
