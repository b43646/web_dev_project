from django.db import models

# Create your models here.


class test(models.Model):
	sum = models.CharField(max_length=254)
	def __unicode__(self):
		return '' + self.sum
