from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class DriverUser(AbstractUser):
	name = models.CharField(max_length=250, default='Name')
	def __str__(self):
		return self.username


# To work this thing delete db.sqlite3
