from django.db import models
from django.contrib.auth.models import User
class  Photo(models.Model) :
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to = 'uploads/')
	upload_date = models.DateTimeField(auto_now=True)