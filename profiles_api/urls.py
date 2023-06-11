from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register("hello-viewset",HelloViewSet,basename="hello-viewset")


app_name = 'profiles_api'

urlpatterns = [
    path('hello-view/',HelloAPIView.as_view()),
    path('',include(router.urls))
]