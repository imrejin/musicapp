from django.db import models


# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=250)
    movie_name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
