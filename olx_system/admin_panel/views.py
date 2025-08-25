from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from .models import StoryOfSystem
from .serializers import StoryOfSystemSerializer

class StoryViews(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request:Request):
        story = StoryOfSystem.objects.all()
        serializer = StoryOfSystemSerializer(story,many=True)
        return Response(serializer.data)

