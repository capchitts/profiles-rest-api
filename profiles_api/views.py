
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

class HelloAPIView(APIView):
    """Test APIView"""


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({
            'message':'hello',
            'an_apiview':an_apiview}
            )

