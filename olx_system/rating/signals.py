from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ratings
from main.models import Ads

@receiver(post_save,sender=Ratings)
def Rating_update(sender,instance,created,**kwargs):
    if created:
        ad = Ads.objects.get(id=instance.ad.id) 
        sum = 0
        for rating in ad.ratings.all():
            sum += rating.rating
        ad.rating = sum/len(ad.ratings.all())
        ad.save()
        