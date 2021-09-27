from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from profile_api import serializer
# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello'})


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'message': 'DELETE'})