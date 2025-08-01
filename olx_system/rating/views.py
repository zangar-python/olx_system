from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializer import RatingsSerializer
from .models import Ratings
from main.models import Ads

# def Rating_result(list):
#     rat = len(list)
#     ratings = sum(list)
#     return ratings/rat

# print(Rating_result([5,5,4,4,5,3,2,2,1,5]))   


class RatingViews(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request:Request):
        if request.data['rating'] > 5.0 or request.data['rating'] < 1.0:
            return Response(data={"error":"оценка больше пяти или меньше одного не ставятся "},status=status.HTTP_400_BAD_REQUEST)
        to_ad = request.data['ad']
        by_ad = Ratings.objects.filter(ad=to_ad)
        ad = Ads.objects.get(id=to_ad)
        if by_ad.filter(user=request.user).exists():
            rating = by_ad.get(user=request.user)
            rating.rating = request.data['rating']
            rating.coment = request.data['coment']
            rating.save()
            serializer = RatingsSerializer(rating)
            return Response(data={'status':"Изменено","data":serializer.data})
        elif not by_ad.filter(user=request.user).exists() :
            rating = Ratings.objects.create(
                ad=ad,
                rating = request.data['rating'],
                coment = request.data['coment'],
                user = request.user
            )
            serializer = RatingsSerializer(rating)
            return Response(data={'status':"Создано","data":serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request:Request):
        ratings = Ratings.objects.all()
        serializer = RatingsSerializer(ratings,many=True)
        return Response(serializer.data)
        