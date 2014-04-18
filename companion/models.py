from django.db import models
from embed_video.fields import EmbedVideoField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Catagories(models.Model):
	catagory = models.CharField(max_length=128)
	def __unicode__(self):
		return self.catagory 

class Topics(models.Model):
	fabCatagory = models.ForeignKey(Catagories)
	topic = models.CharField(max_length=128)
	def __unicode__(self):
		return self.topic 

class Fabrics(models.Model):
	fabTopic = models.ForeignKey(Topics)
	fabName = models.CharField(max_length=128)
	fabContent = models.CharField(max_length=128, blank=True)
	fabWeave = models.CharField(max_length=128, blank=True)
	fabDye = models.CharField(max_length=128, blank=True)
	fabFinish = models.CharField(max_length=128, blank=True)
	fabDescription = models.CharField(max_length=8192) 
	fabImage = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(250, 185)],
                                           format='JPEG',
                                           options={'quality': 60},blank=True) 
	fabImage_secondary = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(500, 370)],
                                           format='JPEG',
                                           options={'quality': 60},blank=True)
	fabVideo = EmbedVideoField(blank=True)
	fabVideoURL = models.URLField(blank=True)
	isPremium = models.BooleanField(default=False)
	def __unicode__(self):
		return self.fabName  
