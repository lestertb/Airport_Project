class Travel:
    def __init__(self, departure, arrival, layover, waitTime, passenger):
        self.departure = departure
        self.arrival = arrival
        self.layover = layover
        self.waitTime = waitTime
        self.timeFlight = 0
        self.price = 0
        self.passenger = passenger
        self.flights = []

    def addFlight(self, flight):
        self.flights.append(flight)

    def calculatePrice(self):
        for v in self.flights:
            self.price = v.price + v.price
        return self.price

    def calculateTimeFlight(self):
        for v in self.flights:
            self.timeFlight = v.timeFlight + v.timeFlight
        return self.timeFlight

    def showFlights(self):
        for flight in self.flights:
            print(flight)