from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cuboid(models.Model):
    length = models.IntegerField()
    breath = models.IntegerField()
    height = models.IntegerField()
    owner = models.ForeignKey('auth.User',related_name='cuboids',on_delete=models.CASCADE)
    created_by = models.CharField(max_length=25)
    last_updated = models.CharField(max_length=25)

    def __str__(self):
        return self.created_by
    
    def save(self,*args,**kwargs):
        super(Cuboid,self).save(*args,**kwargs)
