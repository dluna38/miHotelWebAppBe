from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING


class Reservation(models.Model):

    id = models.BigAutoField(primary_key=True)
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=True)
    guest = models.ForeignKey('guest.Guest',on_delete=DO_NOTHING)
    room = models.ForeignKey('rooms.Rooms',on_delete=CASCADE)
    num_guess= models.SmallIntegerField(null=False,default=1)

    def __str__(self) -> str:
        return '{} - CI:{} - CO:{},gst:{} - room:{}'.format(self.id,self.check_in,self.check_out,self.guest,self.room)