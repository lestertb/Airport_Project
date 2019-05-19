class Travel:
    def __init__(self, departure, arrival, layover, price, passenger):
        self.departure = departure
        self.arrival = arrival
        self.layover = layover
        self.price = price
        self.passenger = passenger
        self.flights = []

    def addFlight(self, flight):
        self.flights.append(flight)