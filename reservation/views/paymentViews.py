from rest_framework import status, views,generics
from rest_framework.response import Response
from ..models.payment import Payment
from ..serializers.paymentSerializer import PaymentSerializer
from rest_framework.permissions import IsAuthenticated

#post
class PaymentCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            if int(serializer.validated_data['amount']) < 0:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer.save()
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
#get
class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)
    
#get
class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['room_number']

#delete
class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)
#put
class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)




