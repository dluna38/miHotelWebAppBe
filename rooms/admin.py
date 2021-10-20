from django.contrib import admin
from .models.user import User
from .models.rooms import Rooms

# Register your models here.
admin.site.register(User)
admin.site.register(Rooms)