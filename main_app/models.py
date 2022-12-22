from django.db import models
from django.urls import reverse 
# Create your models here.
class Lion(models.Model):

	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()


	def get_absolute_url(self):
		return reverse('detail', kwargs={'lion_id': self.id})