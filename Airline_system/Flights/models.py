from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Airport(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64)
    country =models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city} {self.code}'
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    ## duration = models.DurationField(null=True, blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight_class = (
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first', 'First')
    )
    travel_class = models.CharField(max_length=20, choices = flight_class, default = 'economy')

    def __str__(self):
        return f"{self.id} from {self.origin} to {self.destination}"
    
##class Passenger(models.Model):
   
    ## user = ''
    ##flights = models.ManyToManyField(Flight, blank=True, related_name = "passengers")

    ##def __str__(self):
        ##return f"{self.first} ,{self.last}"
 
class GuestBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="bookings")
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length =64)
    email =models.EmailField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name = "booking_flight")
    booking_date = models.DateTimeField()
    ##passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name = "booking_passenger")
    status_choices = (
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
        ('checked_in', 'Checked_In')
    )
    status = models.CharField(max_length= 20, choices = status_choices, default='booked')
    
    
    def __str__(self):
        return f"{self.first_name} have booked flight {self.flight} on this date {self.booking_date}"
 