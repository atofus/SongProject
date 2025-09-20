from django.shortcuts import render
#added this for response
from django.http import HttpResponse

from rest_framework import generics # Allow us to create a class that inherits from a generic API view
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# Where we'll put the code that will be responsible for rednering our views
# or our API endpoints.
# /hello would be an endpoint (location on webserver we're going to)

# When we make our view, we need to have request as param, which will return a response.
# def main(request): 
#     # What will be returned on page once we hit this endpoint.
#     return HttpResponse("<h1>Hello</h1>") 


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all() # Will return all of the room objects
    serializer_class = RoomSerializer # Will use RoomSearlizer which uses serializers.ModelSerializers from serializers.py

    


