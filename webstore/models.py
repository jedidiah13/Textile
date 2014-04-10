from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class StoreCategory(models.Model):
	categoryName = models.CharField(max_length=128)
	def __unicode__(self):
		return self.categoryName 

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
	def __unicode__(self):
		return  self.itemName
	
#class Order(models.Model):
#	item = models.ForeignKey(StoreItem)
#	#how do we create a relation to a user now?
