class FlightMaintenance:
    def __init__(self, airline, departureDate, departureTime, timeFlight, departureAirport, arrivalAirport,
                 plane, gate, track, crewPilot, crewCustomerService, price, layover, type):
        self.airline = airline
        self.departureDate = departureDate
        self.departureTime = departureTime
        self.timeFlight = timeFlight
        self.departureAirport = departureAirport
        self.arrivalAirport = arrivalAirport
        self.plane = plane
        self.gate = gate
        self.track = track
        self.crewPilot = crewPilot
        self.crewCustomerService = crewCustomerService
        self.price = price
        self.layover = layover
        self.type = type
