from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
# This is a class to modify the view of the admin page
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal =("flights",)


admin.site.register(Airport)

# here I specify the class I use to modify the view
admin.site.register(Flight, FlightAdmin)

admin.site.register(Passenger, PassengerAdmin)