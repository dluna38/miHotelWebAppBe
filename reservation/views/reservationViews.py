from datetime import datetime
from rest_framework import status, views,generics
from rest_framework.response import Response
from ..models.reservation import Reservation
from ..serializers.reservationSerializer import ReservationSerializer
from rest_framework.permissions import IsAuthenticated
import pytz
#post
class ReservationCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            if not self.checkReservationsMade(serializer.validated_data['room'],serializer.validated_data['check_in'],serializer.validated_data['check_out']):
                return Response(data={'msg': 'Error con las fechas especificadas'},status=status.HTTP_406_NOT_ACCEPTABLE)

            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def checkReservationsMade(self,room_id,check_in,check_out):
        if check_in > check_out or check_in < datetime.now().replace(tzinfo=pytz.UTC):
            print('El check in es despues del checkout o reserva se intenta hacer en el pasado')
            return False

        filterRoomQuery = Reservation.objects.filter(room=room_id)
        if not filterRoomQuery: return True

        #check rsv on the same date
        if filterRoomQuery.filter(check_in__contains = check_in.date()) | filterRoomQuery.filter(check_out__contains = check_out.date()):
            print('ya existe')
            return False

        #bring two rsv,the closest to check in, in front and behind
        rsvGte = filterRoomQuery.filter(check_in__gte=check_in).order_by('-check_in')[:1]
        rsvLte = filterRoomQuery.filter(check_in__lte=check_in).order_by('-check_in')[:1]

        #check if is between the two closest rsv dates
        rangeRsv= []
        if rsvGte: rangeRsv.append(rsvGte)
        if rsvLte:  rangeRsv.append(rsvLte)
        for rsv in rangeRsv:
            d1 = rsv[0].check_in
            d2 = rsv[0].check_out
            if self.isInBetweenDate(check_in,d1,d2):
                #print('detener {}: {} {}'.format(check_in,d1,d2))
                return False
            elif self.isInBetweenDate(check_out,d1,d2):
                #print('detener {}: {} {}'.format(check_out,d1,d2))
                return False
        
        return True
        
    def isInBetweenDate(self,dateInBetween,date1,date2):
        return date1 <= dateInBetween <= date2

    def get(self,request,*args, **kwargs):
        dic = request.GET.dict()
        try:
            if dic['room'] and dic['check_in'] and dic['check_out']:
                rslt = self.checkReservationsMade(dic['room'], self.formatStrToDate(dic['check_in']),self.formatStrToDate(dic['check_out']))
                return Response(data={'result':rslt})
        except:
            return Response(data={'msg':'No fue posible analizar las fechas'})
    
    def formatStrToDate(self,date):
        try:
            return datetime.strptime(date, '%Y-%m-%dT%H:%M').replace(tzinfo=pytz.UTC)
        except:
            return ""
             
#get
class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
#get
class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all().order_by('-check_in')
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
    

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




