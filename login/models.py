from django.contrib.auth.models import User
from django.db import models
from loginRouter import *
from webstore.models import StoreItem

# This will be helpful to indicate a special price and quantity.
class OrderItem(models.Model):
    itemCost = models.DecimalField(max_digits=16,decimal_places=2)
    itemQuantity = models.IntegerField()
    # The key to a store item. Yep, that works to have a relation to another app
    itemID = models.ForeignKey(StoreItem)
    def __unicode__(self):
        return  self.itemID.itemName
    # this itemcost will be either the regular price or the bookstore price

class Order(models.Model):
    
    orderDate = models.DateTimeField('Order Date')
    shippingCost = models.DecimalField(max_digits=16,decimal_places=2)
    totalCost = models.DecimalField(max_digits=16,decimal_places=2)
    # need to have total cost be calculated automatically based on the items in the order
    item = models.ForeignKey(OrderItem)
    def __unicode__(self):
        return  self.purchaser.user.username + " --- " + unicode(self.orderDate)
    # Need to have shipping cost calcutlated and totalcost be the sum of all of the items




class UserProfile(models.Model):
    user = models.OneToOneField(User)
    confirmation_code = models.CharField(max_length=128)
    reset_code = models.CharField(max_length=128)
    address_lineOne = models.CharField(max_length=128)
    address_lineTwo = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    State = models.CharField(max_length=128)
    zipCode = models.CharField(max_length=10)
    order =  models.ForeignKey(Order)
    def __unicode__(self): 
        return self.user.username    





