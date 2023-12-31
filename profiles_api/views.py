
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from profiles_api import serializers


# Create your views here.

class HelloAPIView(APIView):
    """Test APIView"""

    serializers_class = serializers.HelloSerializer

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
    
    def post(self,request):
        """Create a hello message with name"""
        serializer = self.serializers_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =f'Hello {name}!'
            return Response({"message":message})

        else:
            #return all the errors as per validation rules applied in serializer
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handles Updating an Object"""
        return Response({
            'method':'PUT'
        })
    
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({
            'method':'PATCH'
        })
    
    def delete(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({
            'method':'DELETE'
        })



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, update, partial update, destroy)",
            "Automatically maps to urls using routers",
            "Provides more functionalities with less code!"
        ]

        return Response({
            "message":"Hello",
            "a_viewset":a_viewset
        })
    
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})