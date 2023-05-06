from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    avatar  = models.ImageField(default='avatar.jpg',blank=True,null=True )
    phone=models.CharField(max_length=190 , null=True) 
    
    def __str__(self):
        return f'{self.user.username} Profile'
    

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    