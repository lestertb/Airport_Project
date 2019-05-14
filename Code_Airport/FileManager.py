from FlightMaintenance import *
def save(flightList):
    text = " "
    for flight in flightList:
        text += flight.airline + "$" + str(flight.departureDate) + "$" + str(flight.departureTime) + "$" + \
                str(flight.timeFlight) + "$" + flight.departureAirport + "$" + flight.arrivalAirport + "$" +\
                flight.plane + "$" + flight.gate + "$" + flight.track + "$" + flight.crewPilot + "$" + \
                flight.crewCostumerService + "$" + flight.price + "$" + "$\n"

    try:
        file = open("Flights.txt", "w")
        file.write(text)
        file.close()
    except:
        print("Error trying to download")

def charge():
    result = []
    try:
        file = open("Flights.txt", "r")
        for line in file.readlines():
            data = line.split("$")
            newFlight = FlightMaintenance(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                                          data[8], data[9], data[10], data[11])
            result.append(newFlight)
        file.close()
    except:
        print("Error trying to download")
    return result



