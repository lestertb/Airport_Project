from FlightMaintenance import *
from Record import *
def save(flightList):
    text = " "
    for flight in flightList:
        text += flight.airline + "$" + str(flight.departureDate) + "$" + str(flight.departureTime) + "$" + \
                str(flight.timeFlight) + "$" + flight.departureAirport + "$" + flight.arrivalAirport + "$" +\
                flight.plane + "$" + flight.gate + "$" + flight.track + "$" + flight.crewPilot + "$" + \
                flight.crewCustomerService + "$" + str(flight.price) + "$" + "$\n"

    try:
        file = open("Flights.txt", "w")
        file.write(text)
        file.close()
    except:
        print("Error trying to download ")

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

def saveRecord(recordList):
    text = " "
    for flight in recordList:
        for travel in flight.flights:
            text += flight.passenger +"$" + str(travel.timeFlight)+ "$" + str(travel.departureAirport)+ "$" +\
                    str(flight.waitTime)+"$" + str(travel.arrivalAirport)+"$\n"
    try:
        file = open("Record.txt", "w")
        file.write(text)
        file.close()
    except:
        print("Error trying to download")

def charge1():
    result2 = []
    try:
        file = open("Record.txt", "r")
        for line in file.readlines():
            data = line.split("$")
            newRecord = Travel(data[0],data[1],data[2],data[3],data[4])
            result2.append(newRecord)
        file.close()
    except:
        print("Error trying to download")
    return result2





