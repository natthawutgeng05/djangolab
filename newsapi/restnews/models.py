from django.db import models

# Create your models here.

class NewsPost(models.Model):
    news_text = models.TextField()
    author = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now=True)
