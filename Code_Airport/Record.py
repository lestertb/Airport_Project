class Record:
    def __init__(self, passenger):
        self.passenger = passenger
        self.travels = []

    def addTravel1(self, travel):
        self.travels.append(travel)
