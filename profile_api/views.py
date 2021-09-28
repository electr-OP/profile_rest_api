from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets

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


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializer.HelloSerializer
    
    def list(self, request):

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial)'
            'Automatically maps to URLs using routers'
            'provides more functionality '
        ]
        return Response({'message' : 'Hello', 'a_viewset' : a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

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
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
