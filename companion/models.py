from django.db import models
from embed_video.fields import EmbedVideoField

class Catagories(models.Model):
	catagory = models.CharField(max_length=128)
	def __unicode__(self):
		return self.catagory 

class Topics(models.Model):
	topic = models.CharField(max_length=128)
	def __unicode__(self):
		return self.topic 

class Fabrics(models.Model):
	fabCatagory = models.ForeignKey(Catagories)
	fabTopic = models.ForeignKey(Topics)
	fabName = models.CharField(max_length=128)
	fabContent = models.CharField(max_length=128)
	fabWeave = models.CharField(max_length=128)
	fabDye = models.CharField(max_length=128)
	fabFinish = models.CharField(max_length=128)
	fabDescription = models.CharField(max_length=1024) # is that enough text?
	fabImage = models.ImageField(upload_to='images') # What does upload to do???????????
	fabVideo = EmbedVideoField()