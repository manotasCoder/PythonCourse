from django.urls import path
from . import views

app_name = "flights"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>', views.flight, name="flight"),
    path('add/', views.add, name="add"),
    path('passenger/', views.passenger, name="passenger"),
    path('passengerList/', views.passengerList, name="passengerList"),
    path('book/<int:flight_id>', views.book, name="book")
]