from django.db import models
from django.conf import settings
# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=40, verbose_name='area')
    
    def __str__(self): 
        return self.name   
    class Meta:
      db_table = 'area' 
       

class Rol(models.Model):
    name = models.CharField(max_length=40, verbose_name='rol') 
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self): 
       return self.name   
    class Meta:
      db_table = 'rol'  