from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)
    is_liked = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True,blank=False)
   
    def __str__(self):
       return self.event_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url