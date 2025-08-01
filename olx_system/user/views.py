from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate


from rest_framework import status

from .serializers import UserSerializer

class UserRegisterView(APIView):
    def post(self,request:Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"username":user.username,"password":user.password})
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

class LoginView(APIView):
    def post(self,request:Request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if not user:
            return Response({"error":"Неверные данные!"})
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    
class MyProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request:Request):
        user = request.user
        return Response({"username":user.username,"email":user.email})