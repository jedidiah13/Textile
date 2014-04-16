from django.contrib.auth.models import User
from django.db import models
from loginRouter import *

class ohno(models.Model):
    box = models.CharField(max_length=128)

    def __unicode__(self): 
        return self.user.username    

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    relation = models.OneToOneField(ohno, null=True)
    confirmation_code = models.CharField(max_length=128)
    reset_code = models.CharField(max_length=128)
    address_lineOne = models.CharField(max_length=128)
    address_lineTwo = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    State = models.CharField(max_length=128)
    zipCode = models.CharField(max_length=10)

    def __unicode__(self): 
        return self.user.username    

 

    



