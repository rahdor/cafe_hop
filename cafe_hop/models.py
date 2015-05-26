from django.db import models
from datetime import date, datetime
from django.utils import timezone
import pytz


# Create your models here.


now = datetime.now()

class Cafe(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.name



class Rating(models.Model):
	cafe = models.ForeignKey(Cafe)
	value = models.IntegerField(default = 5)	
	time = models.DateTimeField(default = now)

	def __unicode__(self):
		return str(self.cafe) + str(self.time)



class Comment(models.Model):
	cafe = models.ForeignKey(Cafe)
	text = models.TextField(default = "")
	time = models.DateTimeField(default = now)

	def __unicode__(self):
		return str(self.cafe) + str(self.time)


