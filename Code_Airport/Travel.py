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
        total = 0
        i = 1
        while i < len(self.flights):
            total = self.flights[0].price + "+" + self.flights[1].price
            i = i + 1
        return total

    def calculateTimeFlight(self):
        total = 0
        i = 1
        while i < len(self.flights):
            total = self.flights[0].timeFlight + "+" + self.flights[1].timeFlight
            i = i + 1
        return total

    def showFlights(self):
        for flight in self.flights:
            print(flight)
