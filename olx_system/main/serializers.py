from .models import Ads
from rest_framework.serializers import ModelSerializer

class AdsSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"        