from django.db import models
from django.contrib.auth.models import User

class Train(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_seats = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} ({self.number})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    date_of_journey = models.DateField()
    seats_booked = models.IntegerField()
    payment_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Booking for {self.passenger_name} on {self.train}"
