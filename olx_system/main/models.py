from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATALOG_CHOICES = [
    ("tech","Технология"),
    ("сlothing","Одежда"),
    ("furniture","Мебель"),
    ("automotive","Автотовар"),
    ("tourism","Туризм"),
    ("drugstore","Аптека"),
]

class Ads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ads")
    header = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    body = models.TextField()
    image = models.ImageField(upload_to="images/",blank=False,null=False)
    catalog = models.CharField(max_length=30,choices=CATALOG_CHOICES)
    rating = models.FloatField(default=0.0,null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.username} {self.header}"
    