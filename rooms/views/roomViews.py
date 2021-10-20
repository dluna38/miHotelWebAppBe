from django.conf import settings
from django.http import response
from django.views import View
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from rest_framework import status, views,generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rooms.models.rooms import Rooms
from rooms.serializers.roomsSerializer import RoomsSerializer
from rest_framework.permissions import IsAuthenticated

#post
class RoomCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = RoomsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

#get
class RoomDetailView(generics.RetrieveAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)
#get
class RoomListView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['room_number']

#delete
class RoomDeleteView(generics.DestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)
#put
class RoomUpdateView(generics.UpdateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticated,)




