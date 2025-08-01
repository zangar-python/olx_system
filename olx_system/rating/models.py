from django.db import models

# Create your models here.

from main.models import Ads
from django.contrib.auth.models import User

class Ratings(models.Model):
    ad = models.ForeignKey(Ads,on_delete=models.CASCADE,related_name="ratings")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ratings")
    rating = models.FloatField()
    coment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)