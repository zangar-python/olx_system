from django.urls import path
from .views import AdsPostView,AdsViews,AdView,UpdateAdView,MyAdsViews,CatalogAdsView

urlpatterns = [
    path('',AdsViews.as_view()),
    path('add/',AdsPostView.as_view()),
    path('<int:pk>/',AdView.as_view()),
    path('<int:pk>/update/',UpdateAdView.as_view()),
    path('my/',MyAdsViews.as_view()),
    path('<str:catalog>/',CatalogAdsView.as_view())
]
