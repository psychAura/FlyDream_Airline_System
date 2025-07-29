from django.contrib import admin

from .models import Flight, Airport,  GuestBooking
# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(GuestBooking)