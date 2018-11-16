from django.db import models
from tastypie.models import create_api_key
from django.contrib.auth.models import User


class Person(models.Model):
	#user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length = 15)
	email = models.EmailField()	
	number = models.CharField(max_length = 17)
	gender = models.CharField(max_length = 15)
	date = models.DateField()
	image = models.FileField(upload_to='post_image', blank = True)

	def __str__(self):
		return self.name
    # Create your models here.
models.signals.post_save.connect(create_api_key, sender=User)