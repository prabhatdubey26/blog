from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug =  models.CharField(max_length=130)
    timestamp = models.DateTimeField()