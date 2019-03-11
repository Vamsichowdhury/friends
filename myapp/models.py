from django.db import models

class FriendsCrush(models.Model):
	name=models.CharField(max_length=100)
	crush=models.CharField(max_length=100)

	def __str__(self):
		return self.name