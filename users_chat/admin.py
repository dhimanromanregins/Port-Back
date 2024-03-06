from django.contrib import admin
from .models import CustomUser, Rooms, Message

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Rooms)
admin.site.register(Message)
