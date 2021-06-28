from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flight, Airport, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    return render(request, 'flights/index.html', {
        "flights": flights
    })

def flight(request, flight_id):
    
    flight = Flight.objects.get(id=flight_id)
    people = Passenger.objects.exclude(flights=flight).all()
    return render(request, 'flights/flight.html',{
        'flight':flight,
        "passengers": flight.passengers.all(),
        'people': people
    })

def add(request):
    airports = Airport.objects.all()

    if request.method == 'POST':
        info = request.POST
        originId = info['origin']
        destinationId = info['destination']
        if originId != destinationId:
            originNow = Airport.objects.get(id=originId)
            destinationNow = Airport.objects.get(id=destinationId)
            minutes = info['duration']
            flight = Flight(origin=originNow, destination=destinationNow, duration=minutes)
            flight.save()
            return HttpResponseRedirect(reverse("flights:index") )
        else:
            return render(request, 'flights/add.html',{
            'airports':airports
            })

    return render(request, 'flights/add.html',{
        'airports':airports
    })

def passengerList(request):
    passengers = Passenger.objects.all()
    return render(request, 'passengers/index.html',{
                'passengers': passengers
    })

def passenger(request):
    if request.method=='POST':
        info =request.POST
        name= info['first']
        surname=info['second']
        flightHistory = info.getlist('enroll')
        traveller = Passenger(first=name,last=surname)
        traveller.save()
        if flightHistory:
            for flightid in flightHistory:
                traveller.flights.add(Flight.objects.get(id=flightid))
            return HttpResponseRedirect(reverse("flights:passengerList") )
    flights = Flight.objects.all()
    return render(request, 'passengers/add.html',{
        "flights": flights
    })

def book(request, flight_id):
    if request.method=='POST':
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,) ) )

