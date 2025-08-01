from django.urls import path

from .views import UserRegisterView,LoginView,MyProfile

urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('profile/',MyProfile.as_view())
]
