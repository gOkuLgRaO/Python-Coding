from django.urls import path
from . import views

urlpatterns = [
    path("trains/", views.train_list, name="train_list"),
    path("search/", views.search_trains, name="search_trains"),
    path("book/<int:train_id>/", views.book_train, name="book_train"),
    path("history/", views.booking_history, name="booking_history"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
    path("booking/success/", views.booking_success, name="booking_success"),
    path(
        "download_ticket/<int:booking_id>/",
        views.download_ticket,
        name="download_ticket",
    ),
    path("payment/<int:booking_id>/", views.payment, name="payment"),
]
