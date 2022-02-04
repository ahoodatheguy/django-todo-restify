from django.db import models
from django.utils import timezone


# Create your models here.


class Task(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	date = models.DateTimeField(default=timezone.now())

	def __str__(self) -> str:
		return self.name
