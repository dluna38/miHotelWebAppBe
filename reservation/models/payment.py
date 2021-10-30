from django.db import models
from django.db.models.deletion import DO_NOTHING
from djmoney.models.fields import MoneyField


class Payment(models.Model):

    id = models.BigAutoField(primary_key=True)
    payment_date = models.DateField(null=False)
    payment_type = models.CharField(null=False,max_length=100,default='EFECTIVO')
    payment_status = models.CharField(null=False,max_length=30,default='POR PAGAR')
    amount = MoneyField(max_digits=10,decimal_places=2,default_currency='COP')
    reservation =  models.ForeignKey('Reservation',on_delete=DO_NOTHING)