class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        x = self.capacity - len(self.passengers)
        return x
