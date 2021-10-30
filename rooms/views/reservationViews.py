from rest_framework import status, views,generics
from rest_framework.response import Response
from models.reservation import Reservation
from serializers.reservationSerializer import ReservationSerializer
from rest_framework.permissions import IsAuthenticated

#post
class ReservationCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

#get
class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
#get
class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['room_number']

#delete
class ReservationDeleteView(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
#put
class ReservationUpdateView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)




