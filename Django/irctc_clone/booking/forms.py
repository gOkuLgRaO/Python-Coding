from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BookingForm(forms.ModelForm):
    date_of_journey = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    class Meta:
        model = Booking
        fields = [
            "passenger_name",
            "date_of_journey",
            "seats_booked",
        ]  # Include any other fields you want to expose
