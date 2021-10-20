from rest_framework import serializers
from rooms.models.rooms import Rooms

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'