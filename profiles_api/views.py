from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name  = serializer.validated_data.get('name')
            message = f'Hello {name}' #f is added as prefix to string in order to use variables inside {}
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )
        
        #pk is the primary key, where u want to update the data, can be id
        #but here we arent using the primary key so pk=None
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    #put replaces all the object with the new updated object
    #eg if fname was already there and we do a put request to add lname then it will add lname but fname will be empty if not provided in the request
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    #patch adds to the existing object
    #eg if fname was already there and we do a put request to add lname then it will add lname and the fname will remain intact

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})