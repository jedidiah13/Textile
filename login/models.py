from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from loginRouter import *

# Query for a user's oders:
# first get the user object, then
# usersOrders = userobject.orders_set.all()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    confirmation_code = models.CharField(max_length=128)
    reset_code = models.CharField(max_length=128)
    address_lineOne = models.CharField(max_length=128)
    address_lineTwo = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    State = models.CharField(max_length=128)
    zipCode = models.CharField(max_length=10)
    appExpiryDate = models.DateField(null=True) # user is premium while this in the future

    def __unicode__(self): 
        return unicode(self.user.username)  


class Key(models.Model):
    key = models.CharField(max_length=38)
    active = models.BooleanField()
    owner = models.ForeignKey(UserProfile, null=True)
    keyExpiryDate = models.DateField()

    def __unicode__(self):
        return unicide(self.key)
