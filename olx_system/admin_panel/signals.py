from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from main.models import Ads
from rating.models import Ratings

from .models import StoryOfSystem
@receiver(post_save,sender=Token)
def Logined(sender,instance:Token,created,**kwargs):
    if created:
        StoryOfSystem.objects.create(
            type_of="login",
            info=f"logined with token:{instance.key} user : {instance.user} "
        )
@receiver(post_save,sender=User)
def Registered(sender,instance:User,created,**kwargs):
    if created:
        StoryOfSystem.objects.create(
            type_of="register",
            info=f"'{instance.username}' registered id : {instance.id}"
        )

@receiver(post_save,sender=Ads)
def AdPosted(sender,instance:Ads,created,**kwargs):
    if created:
        StoryOfSystem.objects.create(
            type_of="ad",
            info=f"'{instance.header}' created,user is {instance.user.username},id: {instance.id}"
        )
@receiver(post_save,sender=Ratings)
def RatingAdded(sender,instance:Ratings,created,**kwargs):
    if created:
        StoryOfSystem.objects.create(
            type_of="rating",
            info=f"rating : {instance.rating} ; user : {instance.user.username} id : {instance.id}"
        )


