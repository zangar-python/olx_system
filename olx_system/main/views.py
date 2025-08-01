from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated

from .models import Ads
from .serializers import AdsSerializer

class AdsViews(APIView):
    def get(self,request:Request):
        ads = Ads.objects.all()
        serializer = AdsSerializer(ads,many=True)
        return Response(serializer.data)

class AdsPostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request:Request):
        ad = {
            "user":request.user.id,
            "header":request.data['header'],
            "body":request.data['body'],
            'image':request.data['image'],
            'price':request.data['price'],
            'catalog':request.data['catalog']
        }
        
        serializer = AdsSerializer(data=ad)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AdView(APIView):
    def get(self,request:Request,pk):
        ad = get_object_or_404(Ads,pk=pk)
        serilaizer = AdsSerializer(ad)
        return Response(serilaizer.data)
        # return Response(serilaizer.errors,status.HTTP_400_BAD_REQUEST)
    
class UpdateAdView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request:Request,pk):
        
        ad = get_object_or_404(Ads,pk=pk)
        if request.user == ad.user:
            print(True)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request:Request,pk):
        ad = get_object_or_404(Ads,pk=pk)
        serializer = AdsSerializer(ad,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)   
    def patch(self,request:Request,pk):
        ad = get_object_or_404(Ads,pk=pk)
        serializer = AdsSerializer(ad,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)   

class MyAdsViews(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request:Request):
        my_ads = request.user.ads.all()
        serializer = AdsSerializer(my_ads,many=True)
        return Response(data=serializer.data)

class CatalogAdsView(APIView):
    # catalog
    def get(self,request:Request,catalog:str):
        ads = Ads.objects.filter(catalog=catalog)
        serializer = AdsSerializer(ads,many=True)
        return Response(data=serializer.data)
    # filter
    def post(self,request:Request,catalog:str):
        # max цена
        max = request.data.get("max",10000000)  
        # min цена
        min = request.data.get("min",0)
        # rating
        sort_by_rating = request.data.get("rating",True)
        
        catalog_ads = Ads.objects.filter(catalog=catalog)
        ads = catalog_ads.filter(price__range=(min,max))
        
        if sort_by_rating:
            ads = ads.order_by("-rating")
            
        
        serializer = AdsSerializer(ads,many=True)
        return Response(data=serializer.data)