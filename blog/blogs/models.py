from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    


class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
    



class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    