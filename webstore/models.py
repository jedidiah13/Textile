from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill






class StoreCategory(models.Model):
	categoryName = models.CharField(max_length=128)
	def __unicode__(self):
		return unicode(self.categoryName)

class StoreItem(models.Model):
	
	category = models.ForeignKey(StoreCategory)
	itemName = models.CharField(max_length=128)
	itemNameid = models.CharField(max_length=128)
	description = models.CharField(max_length=2048)
	price = models.DecimalField(max_digits=16,decimal_places=2)
	quantity = models.IntegerField(default=0) 
	#picture = models.ImageField(upload_to='store_images', blank=False)
	picture = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(250, 185)],
                                           format='JPEG',
                                           options={'quality': 60})
	featured_picture = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(800, 300)],
                                           format='JPEG',
                                           options={'quality': 60}, blank=True)
	isFeatured = models.BooleanField(default=False)
	def __unicode__(self):
		return  unicode(self.itemName)


class OrderItem(models.Model):
    itemCost = models.DecimalField(max_digits=16,decimal_places=2)
    itemQuantity = models.IntegerField()
    # The key to a store item. Yep, that works to have a relation to another app
    itemID = models.OneToOneField(StoreItem)
    def __unicode__(self):
        return  unicode(self.itemID.itemName)


class Order(models.Model):
    
    orderDate = models.DateTimeField('Order Date')
    shippingCost = models.DecimalField(max_digits=16,decimal_places=2)
    totalCost = models.DecimalField(max_digits=16,decimal_places=2)
    # need to have total cost be calculated automatically based on the items in the order
    item = models.ForeignKey(OrderItem)
    def __unicode__(self):
        return  unicode(self.item)
	
#class Order(models.Model):
#	item = models.ForeignKey(StoreItem)
#	#how do we create a relation to a user now?
