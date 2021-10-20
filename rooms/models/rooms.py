from django.db import models
from djmoney.models.fields import MoneyField


class Rooms(models.Model):
    ROOM_TYPES = (
        ('IND', 'INDIVIDUAL'),
        ('FAM', 'FAMILIAR'),
        ('DOB', 'DOBLE'),
        ('OTR', 'OTRO'),
    )
    ROOM_STATUS = (
        ('DIS', 'DISPONIBLE'),
        ('OCU', 'OCUPADA'),
        ('MAN', 'MANTENIMIENTO'),
        ('DES', 'DESHABILITADA')
    )
    room_number = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=12, choices=ROOM_TYPES)
    room_description = models.CharField(max_length=100)
    capacity = models.IntegerField(default=1)
    price = MoneyField(max_digits=10, decimal_places= 2, default=0, default_currency='USD')
    status_room = models.CharField(max_length=12, choices=ROOM_STATUS)

