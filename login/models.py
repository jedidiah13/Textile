from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from loginRouter import *
from webstore.models import Order

class OrderTable(models.Model):
    orders = models.ForeignKey(Order)

    def __unicode__(self): 
        return unicode(self.orders)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_orders = models.OneToOneField(OrderTable, null=True)
    confirmation_code = models.CharField(max_length=128)
    reset_code = models.CharField(max_length=128)
    address_lineOne = models.CharField(max_length=128)
    address_lineTwo = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    State = models.CharField(max_length=128)
    zipCode = models.CharField(max_length=10)
    
    def __unicode__(self): 
        return unicode(self.user.username)  

 

    



