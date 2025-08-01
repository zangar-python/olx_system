from django.urls import path

from .views import RatingViews

urlpatterns = [
    path('',RatingViews.as_view())
]
