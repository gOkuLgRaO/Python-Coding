from django.shortcuts import render, get_object_or_404, redirect
from .models import  Train, Booking
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm, UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.db.models import Sum

def train_list(request):
    trains = Train.objects.all()
    return render(request, "booking/train_list.html", {"trains": trains})

def search_trains(request):
    if request.method == "GET":
        origin = request.GET.get("origin")
        destination = request.GET.get("destination")
        trains = Train.objects.filter(origin__icontains=origin, destination__icontains=destination)
        return render(request, "booking/search_results.html", {"trains": trains})


@login_required
def book_train(request, train_id):
    train = Train.objects.get(id=train_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.train = train
            booking.user = request.user

            # Calculate seat availability
            total_booked_seats = (
                Booking.objects.filter(train=train).aggregate(Sum("seats_booked"))[
                    "seats_booked__sum"
                ]
                or 0
            )
            available_seats = train.total_seats - total_booked_seats

            if booking.seats_booked > available_seats:
                messages.error(
                    request,
                    f"Cannot book {booking.seats_booked} seats. Only {available_seats} seats are available.",
                )
            else:
                booking.save()
                # Redirect to payment page after booking
                return redirect("payment", booking_id=booking.id)
    else:
        form = BookingForm()

    # Calculate available seats for display
    total_booked_seats = (
        Booking.objects.filter(train=train).aggregate(Sum("seats_booked"))[
            "seats_booked__sum"
        ]
        or 0
    )
    available_seats = train.total_seats - total_booked_seats

    return render(
        request,
        "booking/book_train.html",
        {"form": form, "train": train, "available_seats": available_seats},
    )


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-date_of_journey")
    return render(request, "booking/booking_history.html", {"bookings": bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking, id=booking_id, user=request.user
    )  # Ensure only the owner can access this booking
    if request.method == "POST":
        train = booking.train
        train.total_seats += booking.seats_booked
        train.save()
        booking.delete()
        return redirect("booking_history")

    return render(request, "booking/cancel_booking.html", {"booking": booking})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "booking/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("train_list")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "booking/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login")

def send_booking_confirmation_email(user_email, booking_details):
    subject = "Booking Confirmation - IRCTC"
    message = f"Dear Customer, \n\nYour booking has been successfully confirmed!\n\nDetails:\n{booking_details}\n\nThank you for using our service."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, email_from, recipient_list)


def booking_success(request):
    return render(request, "booking/booking_success.html")


def download_ticket(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    html = render_to_string("booking/ticket_pdf.html", {"booking": booking})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="ticket_{booking.id}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF")
    return response


@login_required
def payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    if request.method == "POST":
        # Simulate payment completion
        booking.payment_completed = True
        booking.save()

        # Send booking confirmation email after payment
        subject = f"Booking Confirmation for {booking.train.name}"
        message = f"""
        Hi {booking.passenger_name},

        Your booking is confirmed for {booking.train.name} ({booking.train.number}).
        Date of Journey: {booking.date_of_journey}
        Number of Seats Booked: {booking.seats_booked}

        Thank you for using our service!
        """
        recipient_email = request.user.email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

        messages.success(request, "Payment successful! Your booking is confirmed.")
        return redirect("booking_history")  # Redirect to booking history after payment

    return render(request, "booking/payment.html", {"booking": booking})
