from django.db import models
from django.utils import timezone, dateformat
import datetime

class Author(models.Model):
    name =models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.surname

class Post(models.Model):
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='hairclip', verbose_name='photo', blank=True)
    published_date = models.DateTimeField(
            default=timezone.now)
    quantity=models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return self.title
