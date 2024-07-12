from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class  Post(models.Model) :
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')