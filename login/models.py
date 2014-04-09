from django.contrib.auth.models import User
from django.db import models
from loginRouter import *

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    confirmation_code = models.CharField(max_length=128)
    def __unicode__(self):
		return self.user.username    
    



