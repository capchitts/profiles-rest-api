from django.urls import path
from .views import *

app_name = 'profiles_api'

urlpatterns = [
    path('hello-view/',HelloAPIView.as_view())
]