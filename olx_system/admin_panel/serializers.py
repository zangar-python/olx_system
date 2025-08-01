from rest_framework.serializers import ModelSerializer
from .models import StoryOfSystem

class StoryOfSystemSerializer(ModelSerializer):
    class Meta:
        model = StoryOfSystem
        fields = "__all__"