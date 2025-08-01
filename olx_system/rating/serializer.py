from .models import Ratings
from rest_framework.serializers import ModelSerializer

class RatingsSerializer(ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'