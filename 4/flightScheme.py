from flight import Flight

flight = Flight(3)

boarders = ["Pepe","Maria","Juan","Cierva"]

for person in boarders:
    success = flight.addPassenger(person)
    if success:
        print(f'Thank you {person} for joining Coder Airlines, have a nice flight') 
    else:
        print(f'full capacity reached, unfortunately {person} cannot board this flight')

