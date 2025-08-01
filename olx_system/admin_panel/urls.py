from django.urls import path
from .views import StoryViews

urlpatterns = [
    path('story/',StoryViews.as_view())
]
