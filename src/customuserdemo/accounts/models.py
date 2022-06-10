from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.email 
    
