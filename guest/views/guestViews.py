from rest_framework import status, views,generics
from rest_framework.response import Response
from ..models.guest import Guest
from ..serializers.guestSerializer import GuestSerializer
from rest_framework.permissions import IsAuthenticated

#post
class GuestCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

#get
class GuestDetailView(generics.RetrieveAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAuthenticated,)
#get
class GuestListView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['room_number']

#delete
class GuestDeleteView(generics.DestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAuthenticated,)
#put
class GuestUpdateView(generics.UpdateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAuthenticated,)




