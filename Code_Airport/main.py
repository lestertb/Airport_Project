""""------------------------------------------#Imports---------------------------------------"""


from datetime import (date, datetime, timedelta)
from User import *
from TrackMaintenance import *
from GateMaintenance import *
from AirlineMaintenance import *
from crewMaintenance import *
from PlaneMaintenance import *
from AirportMaintenance import *
from FileManager import *
from collections import Counter
import random

'------------------------------------------#Lists---------------------------------------'

#Declaration of global lists
usersList = []
trackList = []
gateList = []
airlineList = []
crewList = []
airportList = []
aircraftList = []
flightList = []
pilotsList = []
costumersServerList = []
gateListFlight = []
aircraftListFlight = []
listDates = []
listgates = []



"""#Data to inject
userTest = User("lester", 18, "lestertb", "123", "111", 1)
usersList.append(userTest)

trackTest = MaintenenceTracks("10", "Available")
trackList.append(trackTest)

trackTest1 = MaintenenceTracks("11", "Available")
trackList.append(trackTest1)

gateTest1 = MaintenanceGates("10", "Available")
gateList.append(gateTest1)

gateTest = MaintenanceGates("11", "Available")
gateList.append(gateTest)

airlineTest = AirlineMaintenance("primera", 2019, "Local", 10)
airlineList.append(airlineTest)

crewTest1 = CrewMaintenance("leo1", 18, 11, "primera", "Pilot", "Available")
crewList.append(crewTest1)

crewTest2 = CrewMaintenance("leo2", 18, 12, "primera", "Pilot", "Available")
crewList.append(crewTest2)

crewTest3 = CrewMaintenance("leo3", 18, 13, "primera", "Pilot", "Available")
crewList.append(crewTest3)

crewTest4 = CrewMaintenance("leo4", 18, 14, "primera", "Costumer service", "Available")
crewList.append(crewTest4)

crewTest5 = CrewMaintenance("leo5", 18, 15, "primera", "Costumer service", "Available")
crewList.append(crewTest5)

crewTest6 = CrewMaintenance("leo6", 18, 16, "primera", "Costumer service", "Available")
crewList.append(crewTest6)

crewTest7 = CrewMaintenance("leo7", 18, 17, "primera", "Costumer service", "Available")
crewList.append(crewTest7)

crewTest8 = CrewMaintenance("leo8", 18, 18, "primera", "Costumer service", "Available")
crewList.append(crewTest8)

crewTest9 = CrewMaintenance("leo9", 18, 19, "primera", "Costumer service", "Available")
crewList.append(crewTest9)

crewTest10 = CrewMaintenance("leo10", 18, 20, "primera", "Costumer service", "Available")
crewList.append(crewTest10)

crewTest11 = CrewMaintenance("leo11", 18, 20, "primera", "Costumer service", "Available")
crewList.append(crewTest11)

crewTest12 = CrewMaintenance("leo12", 18, 21, "primera", "Pilot", "Available")
crewList.append(crewTest12)

crewTest13 = CrewMaintenance("leo13", 18, 21, "primera", "Costumer service", "Available")
crewList.append(crewTest13)

crewTest14 = CrewMaintenance("leo14", 18, 22, "primera", "Costumer service", "Available")
crewList.append(crewTest14)

crewTest15 = CrewMaintenance("leo15", 18, 23, "primera", "Costumer service", "Available")
crewList.append(crewTest15)

crewTest16 = CrewMaintenance("leo16", 18, 24, "primera", "Pilot", "Available")
crewList.append(crewTest16)

crewTest17 = CrewMaintenance("leo17", 18, 25, "primera", "Pilot", "Available")
crewList.append(crewTest17)

crewTest18 = CrewMaintenance("leo18", 18, 26, "primera", "Costumer service", "Available")
crewList.append(crewTest18)

airportTest1 = AirportMaintenance("ppp", "pppp", "ppppp")

airportList.append(airportTest1)

airportTest2 = AirportMaintenance("sss", "ssss", "sssss")
airportList.append(airportTest2)

aircraftTest = PlaneMaintenance("first", 2019, "1", "primera", 10, "Available")
aircraftList.append(aircraftTest)

aircraftTest1 = PlaneMaintenance("second", 2019, "2", "primera", 10, "Available")
aircraftList.append(aircraftTest1)

aircraftTest2 = PlaneMaintenance("third", 2019, "3", "primera", 10, "Available")
aircraftList.append(aircraftTest2)"""


'------------------------------------------#Rules or Variables---------------------------------------'
"""strDate = '2/4/18'
objDate = datetime.strptime(strDate, '%m/%d/%y')
objDate
datetime.datetime(2018, 2, 4, 0, 0)
datetime.strftime(objDate,'%b %d, %Y')
'Feb 04, 2018'
datetime.strftime(objDate,'%Y')"""

'------------------------------------------#Fuctions---------------------------------------'

#Procedure to add Users in the User object
def addUser(name, age, email, id, password, role):
    newUser = User(name, age, email, id, password, role)
    usersList.append(newUser)

#Procedure to show the info of user
def showInfoUser():
    if usersList != []:
        for user in usersList:
            print("Name: ", user.name, "Age: ", user.age,
                  "Email: ", user.email, "ID: ", user.id,
                  "Password:", user.password, "Role:", user.role)
    else:
        print("\nNo users found\n")

#Procedure to verify the id is not repeated
def verifyID(id):
    for user in usersList:
        if id == user.id:
            return True
    else:
        return False

#Procedure to verify the Email is not repeated
def verifyEmail(email):
    for user in usersList:
        if email == user.email:
            return True
    else:
        return False

#Procedure to validate the login
def logIn(id, password):
    listausers = usersList
    while usersList != []:
        for user in listausers:
            if user.id == id and user.password == password:
                role = user.role
                if role == 1:
                    return role
                else:
                    return role
        else:
            return "\n User not found, Please Sign up\n"
    return "\n User not found, Please Sign up\n"

#Procedure to add a track in the Track object
def addTrack(number, status):
    newTrack = MaintenenceTracks(number, status)
    trackList.append(newTrack)

#Procedure to verify the track is not repeated
def verifyTrack(number):
    for track in trackList:
        if number == track.number:
            return True
    else:
        return False

#Procedure to show the tracks
def showTracks():
    if trackList != []:
        for track in trackList:
            print("Track Number: ", track.number, "Status: ", track.status)
    else:
        print("\nNo tracks found\n")

#Procedure to modify the track
def modifyTrack(number, status):
    for track in trackList:
        if track.number == number:
            track.status = status
            return "\nSuccessful modification\n"
    else:
        return "\nTrack not found\n"

#Procedure to delete a Track
def deleteTrack(number):
    for track in trackList:
        if number == track.number:
            trackList.remove(track)
            return "\nSuccessful delete\n"
    else:
        return "\nTrack no found\n"

#Procedure to add a gate in the Gate object
def addGate(number,status):
    newGate = MaintenanceGates(number, status)
    gateList.append(newGate)

#Procedure to verify the gate is not repeated
def verifyGate(number):
    for gate in gateList:
        if number == gate.number:
            return True
    else:
        return False

#Procedure to verify the gate of the flight exist
def verifyGateFlight(number):
    for gate in gateListFlight:
        if number == gate.number:
            return True
    else:
        return False

#Procedure to push in listGateFlight
def pushListGateFlight(number):
    for gate in gateList:
        if number == gate.number:
            gateListFlight.append(gate)

#Procedure to verify the plaen of the flight exist
def verifyPlaneFlight(model):
    for aircraft in aircraftListFlight:
        if model == aircraft.model:
            return True
    else:
        return False

#Procedure to push in listPlaneFlight
def pushListPlaneFlight(model):
    for aircraft in aircraftList:
        if model == aircraft.model:
            aircraftListFlight.append(aircraft)

#Procedure to show the Gate info
def showGates():
    if gateList != []:
        for gate in gateList:
            print("Gate number:", gate.number, "Gate status:", gate.status)
    else:
        print("\nNo gates found\n")

#Procedure to modify a gate
def modifyGate(number,status):
    for gate in gateList:
        if number == gate.number:
            gate.status = status
            return "\nSuccessful modification\n"
    else:
        return "\nGate not found\n"

#Procedure to delete a gate
def deleteGate(number):
    for gate in gateList:
        if number == gate.number:
            gateList.remove(gate)
            return "\nSuccesful delete\n"
    else:
        return "\nGate not found\n"

#Procedure to add a airline
def addAirline(name, foundationYear, type, operationCountries):
    newAirline = AirlineMaintenance(name, foundationYear, type, operationCountries)
    airlineList.append(newAirline)

#Procedure to verify a airline name is unique
def verifyAirline(name):
    for airline in airlineList:
        if name == airline.name:
            return True
    else:
        return False

#Procedure to show airline info
def showAirlines():
    if airlineList != []:
        for airline in airlineList:
            print("Name: ", airline.name, "Foundation Year: ", airline.foundationYear,
                  "Type: ", airline.type, "Number of countries where it operates: ", airline.operationCountries)
    else:
        print("\nNo airlines found\n")

#Procedure to modify a airline
def modifyAirline(name, foundationYear, type, operationCountries):
    for airline in airlineList:
        if name == airline.name:
            airline.foundationYear = foundationYear
            airline.type = type
            airline.operationCountries = operationCountries
            return "\nSuccessful modification\n"
    else:
        return "\nAirline not found\n"

#Procedure to delete a airline
def deleteAirline(name):
    for airline in airlineList:
        if name == airline.name:
            airlineList.remove(airline)
            return "\nSuccesful delete\n"
    else:
        return "\nAirline not found\n"

#Procedure to add a crew
def addCrewmember (name, age, id, airline, type,status):
    newCrewmbember = CrewMaintenance(name, age, id, airline, type, status)
    crewList.append(newCrewmbember)

#Procedure to verify the crew
def verifyCrewmember(id):
    for member in crewList:
        if id == member.id:
            return True
    else:
        return False

#Procedure to show the crew info
def showCrew():
    if crewList != []:
        for crew in crewList:
            print("Name: ", crew.name, "Age: ", crew.age, "Identification card: ", crew.id,
                  "Airline: ", crew.airline, "Type: ", crew.type, "Status: ", crew.status)
    else:
        print("\nCrew not found\n")

#Procedure to delete a crew
def deleteCrew(id):
    for crew in crewList:
        if id == crew.id:
            crewList.remove(crew)
            return "\nSuccesful delete\n"
    else:
        return "\nCrewmember not found\n"

#Procedure to modify
def modifyCrew(id,name,age,airline,type,status):
    for crew in crewList:
        if id == crew.id:
            crew.age = age
            crew.name = name
            crew.airline = airline
            crew.type = type
            crew.status = status

            return "\nSuccessful modification\n"
    else:
        return "\nCrewmember not found\n"

#Procedure to add
def addAircraft(model,creationyear,id,airline,capacity,status):
    newAircraft = PlaneMaintenance(model, creationyear, id, airline, capacity, status)
    aircraftList.append(newAircraft)

#Procedure to verify
def verifyAircraft(id):
    for aircraf in aircraftList:
        if id == aircraf.id:
            return True
    else:
        return False

#Procedure to show info
def showAircraft():
    if aircraftList != []:
        for aircraft in aircraftList:
            print("Model:", aircraft.model, "Creation year:", aircraft.creationyear,
                  "ID:", aircraft.id, "Airline:", aircraft.airline, "Capacity:", aircraft.capacity,
                  "Status:", aircraft.status)
    else:
        print("\nAircraft not found\n")

#Procedure to delete
def deleteAircraft(id):
    for aircraft in aircraftList:
        if id == aircraft.id:
            aircraftList.remove(aircraft)
            return "\nSuccesful delete\n"
    else:
        return "\nAircraft not found\n"


def modifyAircraft(id,model,creationyear,airline,capacity,status):
    for aircraft in aircraftList:
        if id == aircraft.id:
            aircraft.model = model
            aircraft.creationyear = creationyear
            aircraft.airline = airline
            aircraft.capacity = capacity
            aircraft.status = status
            return "\nSuccesful modification\n"
    else:
        return "\nAircraft not found\n"


def addAirport(name, city, country):
    newAirport = AirportMaintenance(name, city, country)
    airportList.append(newAirport)


def showAirport():
    if airportList != []:
        for airport in airportList:
            print("Name:", airport.name, "City:", airport.city, "Country:", airport.country)
    else:
        print("\nAircraft not found\n")


def verifyAirport(name):
    for airport in airportList:
        if name == airport.name:
            return True
    else:
        return False


def verifyDepartureDate(departureDate):
    minimum = datetime.today()
    date = datetime.strftime(minimum, '%d/%m/%Y')
    if departureDate < date:
        return False
    else:
        return True


def deleteAirport(name):
    for airport in airportList:
        if name == airport.name:
            airportList.remove(airport)
            return "\nSuccesful delete\n"
    else:
        return "\nAirport not found\n"


def modifyAirport(name, city, country):
    for airport in airportList:
        if name == airport.name:
            airport.city = city
            airport.country = country
            return "\nSuccesful modification\n"
    else:
        return "\nAirport not found\n"


def automaticPlane():
    for aircraft in aircraftList:
        if aircraft.status == "Available":
            return aircraft.model
    else:
        return False


def automaticGate():
    for gate in gateList:
        if gate.status == "Available":
            return gate.number
    else:
        return False


def dailyFlight(departureDate):
    i = 0
    departureDate2 = datetime.strptime(departureDate, '%d/%m/%Y')
    day = timedelta(days=1)
    oneDayLater = departureDate2 + day
    pilot1 = pilotsList[i].name
    pilot2 = pilotsList[i+1].name
    costumersServer1 = costumersServerList[i].name
    costumersServer2 = costumersServerList[i+1].name
    costumersServer3 = costumersServerList[i+2].name
    while departureDate2 < oneDayLater:
        for crew in crewList:
            if crew.name == pilot1:
                crew.status = "In service"
            elif crew.name == pilot2:
                crew.status = "In service"
            elif crew.name == costumersServer1:
                crew.status = "In service"
            elif crew.name == costumersServer2:
                crew.status = "In service"
            elif crew.name == costumersServer3:
                crew.status = "In service"
            else:
                return False
    else:
        for crew in crewList:
            if crew.name == pilot1:
                crew.status = "Available"
            elif crew.name == pilot2:
                crew.status = "Available"
            elif crew.name == costumersServer1:
                crew.status = "Available"
            elif crew.name == costumersServer2:
                crew.status = "Available"
            elif crew.name == costumersServer3:
                crew.status = "Available"

def aircraftUse(departureTime, timeFlight, plane):
    hour = '1'
    hour = datetime.strptime(hour, '%H')
    hour2 = '0'
    hour2 = datetime.strptime(hour2, '%H')
    departureTime = datetime.strptime(departureTime, '%H:%M')
    timeFlight = datetime.strptime(timeFlight, '%H:%M')
    hourBefore = departureTime - hour
    durationTime = hourBefore + timeFlight
    departureTime2 = departureTime - hour2
    durationTime2 = durationTime - hour2
    while departureTime2 > hourBefore and departureTime2 < durationTime2:
        for aircraft in aircraftList:
            if aircraft.model == plane:
                aircraft.status = "In service"
                return True
    else:
        for aircraft in aircraftList:
            if aircraft.model == plane:
                aircraft.status = "Available"


def automaticTrack():
    for track in trackList:
        if track.status == "Available":
            return track.number
    else:
        return False


def automaticCrewPilots(airline):
    for crew in crewList:
        if crew.airline == airline and crew.status == "Available" and crew.type == "Pilot":
            pilotsList.append(crew)



def automaticCrewCostumerService(airline):
    for crew in crewList:
        if crew.airline == airline and crew.status == "Available" and crew.type == "Costumer service":
            costumersServerList.append(crew)


def getPilots():
    i = 0
    if pilotsList != []:
            x = "Names: {0} {1}".format(pilotsList[i].name, pilotsList[i+1].name)
            for a in crewList:
                if a.name == pilotsList[i].name:
                    a.status = "In service"
                elif a.name == pilotsList[i+1].name:
                    a.status = "In service"
            return x
    else:
        return False


def getCostumersServer():
    i = 0
    if costumersServerList != []:
            for a in crewList:
                if a.name == costumersServerList[i].name:
                    a.status = "In service"
                elif a.name == costumersServerList[i+1].name:
                    a.status = "In service"
                elif a.name == costumersServerList[i+2].name:
                    a.status = "In service"
            return costumersServerList[i].name + ", " + costumersServerList[i+1].name\
                   + " and " + costumersServerList[i+2].name
    else:
        return False


def addFlight(airline, departureDate, departureTime, timeFlight, departureAirport, arrivalAirport, plane, gate, track,
              crewPilot, crewCustomerService, price):
    newFlight = FlightMaintenance(airline, departureDate, departureTime, timeFlight, departureAirport, arrivalAirport,
                                  plane, gate, track, crewPilot, crewCustomerService, price)
    flightList.append(newFlight)


def modifyStatusGate(gate1, departureTime):
    hour = '1'
    hour = datetime.strptime(hour, '%H')
    h1 = datetime.strptime(departureTime, '%H:%M')
    result = h1 - hour
    while result != None:
        for gate in gateList:
            if gate.number == gate1:
                gate.status = "In use"
        else:
            return False


def showFlights():
    if flightList != []:
        for flight in flightList:
            print("\nInfo Flight\n"
                  "\nAirline:", flight.airline,
                  "\nDeparture Date:", flight.departureDate,
                  "\nDeparture Time:", flight.departureTime,
                  "\nTime of flight:", flight.timeFlight,
                  "\nDeparture Airport:", flight.departureAirport,
                  "\nArrival Airport:", flight.arrivalAirport,
                  "\nAircraft:", flight.plane,
                  "\nGate:", flight.gate,
                  "\nTrack:", flight.track,
                  "\nCrewPilots:", flight.crewPilot,
                  "\nCrewCustomerService:", flight.crewCustomerService)
    else:
        print("\nFlights not found\n")


def deleteFlight (departureDate, departureTime, gate, plane):
    i = 0
    for flight in flightList:
        if flight.departureDate == departureDate and flight.departureTime == departureTime:
            flightList.remove(flight)
            pilot1 = pilotsList[i].name
            pilot2 = pilotsList[i + 1].name
            costumersServer1 = costumersServerList[i].name
            costumersServer2 = costumersServerList[i + 1].name
            costumersServer3 = costumersServerList[i + 2].name
            for crew in crewList:
                if crew.name == pilot1:
                    crew.status = "Available"
                elif crew.name == pilot2:
                    crew.status = "Available"
                elif crew.name == costumersServer1:
                    crew.status = "Available"
                elif crew.name == costumersServer2:
                    crew.status = "Available"
                elif crew.name == costumersServer3:
                    crew.status = "Available"
            for a in gateList:
                if a.number == gate:
                    a.status = "Available"
            for b in aircraftList:
                if b.model == plane:
                    b.status = "Available"
            return "\nSuccesful delete\n"
    else:
        return "\nFlight not found\n"


def modifyFlight(departureDate,departureTime,departureDate2,departureTime2,timeFlight,departureAirport,arrivalAirport):
    for flight in flightList:
        if flight.departureDate == departureDate and flight.departureTime == departureTime:
            flight.departureDate = departureDate2
            flight.departureTime = departureTime2
            flight.timeFlight = timeFlight
            flight.departureAirport = departureAirport
            flight.arrivalAirport = arrivalAirport
            return "\nSuccesful modification\n"
    else:
        return "\nFlight not found\n"

def firstReport(date1, date2):
    datetime.strptime(date1, '%d/%m/%Y')
    datetime.strptime(date2, '%d/%m/%Y')
    for dateflight in listDates:
        datetime.strptime(dateflight, '%d/%m/%Y')
        if date1 < dateflight and dateflight < date2:
            for flight in flightList:
                if flight.departureDate == dateflight:
                    print("\nInfo Flight\n"
                          "\nAirline:", flight.airline,
                          "\nDeparture Date:", flight.departureDate,
                          "\nDeparture Time:", flight.departureTime,
                          "\nTime of flight:", flight.timeFlight,
                          "\nDeparture Airport:", flight.departureAirport,
                          "\nArrival Airport:", flight.arrivalAirport,
                          "\nAircraft:", flight.plane,
                          "\nGate:", flight.gate,
                          "\nTrack:", flight.track,
                          "\nCrewPilots:", flight.crewPilot,
                          "\nCrewCustomerService:", flight.crewCustomerService)
    else:
        print("No flights were found between those dates")

def secondReport(gate):#This function looks for the number of flights that have a specific door
    for flight in flightList:
        if flight.gate == gate:
            print("\nInfo Flight\n"
                 "\nAirline:", flight.airline,
                 "\nDeparture Date:", flight.departureDate,
                 "\nDeparture Time:", flight.departureTime,
                 "\nTime of flight:", flight.timeFlight,
                 "\nDeparture Airport:", flight.departureAirport,
                 "\nArrival Airport:", flight.arrivalAirport,
                 "\nAircraft:", flight.plane,
                 "\nGate:", flight.gate,
                 "\nTrack:", flight.track,
                 "\nCrewPilots:", flight.crewPilot,
                 "\nCrewCustomerService:", flight.crewCustomerService)
    else:
       print("\nNot boarding gates found\n")

def thirdReport():
    i = 0
    cont = 0
    while i < len(airportList):
        for flight in flightList:
            if flight.departureAirport == airportList[i].name:
                cont += 1
        print("Name:", airportList[i].name, "Cuantity: ", cont)
        i += 1

def fourthReport():
    cont = 0
    cont2 = 0
    for crew in crewList:
        for costumer in costumersServerList:
            if costumer == crew.name:
                cont = cont + 1
        else:
            for pilot in pilotsList:
                if pilot == crew.name:
                    cont2 = cont2 + 1
        if crew.type == "Pilot":
            print(crew.name, cont2)
        if crew.type == "Costumer service":
            print(crew.name, cont)

def verifyDates(firstDate, secondDate):
    firstDate = datetime.strptime(firstDate, '%d/%m/%Y')
    secondDate = datetime.strptime(secondDate, '%d/%m/%Y')
    if firstDate < secondDate:
        return True
    else:
        return False
'------------------------------------------#Menus---------------------------------------'


def trackStatusMenu():
    print("Select the track status.\n"
          "1)Available.\n"
          "2)Not Available.\n"
          "3)In maintenance.\n")
    option = input("Enter the option to the status:")
    if option == "1":
        return "Available"

    elif option == "2":
        return "Not Available"

    elif option == "3":
        return "In maintenance"

    else:
        print("Invalid option")
        return trackStatusMenu()


def gateStatusMenu():
    print("Select the gate status.\n"
          "1)Available.\n"
          "2)In use.\n"
          )
    option = input("Enter the option to the status:")
    if option == "1":
        return "Available"

    elif option == "2":
        return "In use"

    else:
        print("Invalid option")
        return gateStatusMenu()


def typeAirlineMenu():
    print("Select the type of airline.\n"
          "1)International.\n"
          "2)Local.\n")
    option = input("Enter the option to the type:")
    if option == "1":
        return "International"

    elif option == "2":
        return "Local"

    else:
        print("Invalid option")
        return typeAirlineMenu()


def crewRoleMenu():
    print("Select the role of the crewmember.\n"
          "1)Pilot.\n"
          "2)Costumer service.\n")
    option = input("Enter the option for the role:")
    if option == "1":
        return "Pilot"

    elif option == "2":
        return "Costumer service"

    else:
        print("Invalid option")
        return crewRoleMenu()


def crewStatusMenu():
    print("Select the status of the crewmember.\n"
          "1)Available.\n"
          "2)In service.\n")
    option = input("Enter the option for the status:")
    if option == "1":
        return "Available"

    elif option == "2":
        return "In service"

    else:
        print("Invalid option")
        return crewStatusMenu()


def crewAirlineMenu():
    i = 0
    x = 1
    while i < len(airlineList):
        print(x, ")", airlineList[i].name)
        x += 1
        i += 1

def airportMenu():
    i = 0
    x = 1
    while i < len(airportList):
        print(x, ")", airportList[i].name)
        x += 1
        i += 1

def aircraftAirlineMenu():
    i = 0
    x = 1
    while i < len(airlineList):
        print(x, ")", airlineList[i].name)
        x += 1
        i += 1


def aircraftStatusMenu():
    print("Select the status of the aircraft.\n"
          "1)Available.\n"
          "2)In service.\n")
    option = input("Enter the option for the status:")
    if option == "1":
        return "Available"

    elif option == "2":
        return "In service"

    else:
        print("Invalid option")
        return aircraftStatusMenu()


def maintenanceTracks(role):
    if role == 1:
        role = 1
        print("Maintenance of Tracks.\n",
              "1)Create Tracks.\n",
              "2)See Tracks.\n",
              "3)Modify Tracks.\n",
              "4)Delete Tracks.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            i = 1
            while True:
                try:
                    x = int(input("Enter the number of the tracks you are going to add:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            while i <= x:
                number = input("Enter number of the track:")
                if verifyTrack(number) == True:
                    while verifyTrack(number) == True:
                        print("Track already exists, try again")
                        number = input("Enter number of the track:")
                        if verifyTrack(number) == False:
                            break
                status = trackStatusMenu()
                addTrack(number, status)
                i = i + 1

        elif option == "2":
            showTracks()

        elif option == "3":
            showTracks()
            number = input("Enter the Track number to modify:")
            status = trackStatusMenu()
            print(modifyTrack(number, status))

        elif option == "4":
            showTracks()
            number = input("Enter number of the track to delete")
            print(deleteTrack(number))

        elif option == "5":
            mainMenu(role)

        else:
            print("Invalid option")
        maintenanceTracks(role)
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the tracks\n")
        print("\nMaintenance of Tracks.\n",
              "1)See Tracks.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showTracks()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        maintenanceTracks(role)


def maintenanceGates(role):
    if role == 1:
        role = 1
        print("Maintenance of boarding gates.\n",
              "1)Create Gates.\n",
              "2)See Gates.\n",
              "3)Modify Gates.\n",
              "4)Delete Gates.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            i = 1
            while True:
                try:
                    x = int(input("Enter the number of the gate you are going to add:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            while i <= x:
                number = input("Enter number of the gate:")
                if verifyGate(number) == True:
                    while verifyGate(number)== True:
                        print("This gate already exist, try again")
                        number = input("Enter number of the gate")
                        if verifyGate(number)== False:
                            break
                status = gateStatusMenu()
                addGate(number, status)
                i += 1
        elif option == "2":
            showGates()

        elif option == "3":
            showGates()
            number = input("Enter the Gate number to modify:")
            status = gateStatusMenu()
            print(modifyGate(number, status))

        elif option == "4":
            showGates()
            number = input("Enter number of the gate to delete")
            print(deleteGate(number))

        elif option == "5":
            mainMenu(role)
        else:
            print("Invalid option")
        maintenanceGates(role)
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the Gates\n")
        print("\nMaintenance of Gates.\n",
              "1)See Gates.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showGates()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        maintenanceGates(role)


def airlineMaintenance(role):
    if role == 1:
        role = 1
        print("Airline Maintenance.\n",
              "1)Create Airline.\n",
              "2)See Airline.\n",
              "3)Modify Airline.\n",
              "4)Delete Airline.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            i = 1
            while True:
                try:
                    x = int(input("Enter the number of the airlines you are going to add:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            while i <= x:
                name = input("Enter name of the Airline:")
                if verifyAirline(name) == True:
                    while verifyAirline(name) == True:
                        print("Airline already exists, try again")
                        name = input("Enter name of the Airline:")
                        if verifyAirline(name) == False:
                            break
                while True:
                    try:
                        foundationYear = input('\n Enter the foundation year ==> Example: "2000"')
                        datetime.strptime(foundationYear, '%Y')
                        break
                    except:
                        print("\n You have not entered a correct year")
                type = typeAirlineMenu()
                while True:
                    try:
                        operationCountries = int(input("Enter the number of countries where it operates:"))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                addAirline(name, foundationYear, type, operationCountries)
                i = i + 1

        elif option == "2":
            showAirlines()

        elif option == "3":
            showAirlines()
            name = input("Enter the Airline name to modify:")
            while True:
                try:
                    foundationYear = input("Enter the new foundation year or the same:")
                    datetime.strptime(foundationYear, '%Y')
                    break
                except:
                    print("\n You have not entered a correct year")
            type = typeAirlineMenu()
            while True:
                try:
                    operationCountries = int(input("Enter the number of countries where it operates"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            print(modifyAirline(name, foundationYear, type, operationCountries))

        elif option == "4":
            showAirlines()
            name = input("Enter the name of the airline to delete:")
            print(deleteAirline(name))

        elif option == "5":
            mainMenu(role)

        else:
            print("Invalid option")
        airlineMaintenance(role)
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the airlines\n")
        print("\nMaintenance of Airlines.\n",
              "1)See Airlines.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showAirlines()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        airlineMaintenance(role)


def crewMaintenance(role):
    if role == 1:
        role = 1
        print("Crew Maintenance.\n",
              "1)Create Crewmember.\n",
              "2)See Crewmembers.\n",
              "3)Modify Crewmember.\n",
              "4)Delete Crewmember.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            i = 1
            while True:
                try:
                    x = int(input("Enter the number of the persons you are going to add:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            while i <= x:
                name = input("Enter name of the person:")
                while True:
                    try:
                        age = int(input("Enter age of the person:"))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                id = input("Enter identification card:")
                if verifyCrewmember(id) == True:
                    while verifyCrewmember(id) == True:
                        print("This person already exists, try again")
                        id = input("Enter identification card of the person:")
                        if verifyCrewmember(id) == False:
                            break
                crewAirlineMenu()
                airline = input("Enter the name of the airline which it belongs:")
                if verifyAirline(airline) == False:
                    while verifyAirline(airline) == False:
                        print("This airline doesn't exist, try again")
                        airline = input("Enter the name of the airline which it belongs:")
                        if verifyAirline(airline) == True:
                            break
                type = crewRoleMenu()
                status = crewStatusMenu()
                addCrewmember(name, age, id, airline, type, status)
                i += 1
        elif option == "2":
            showCrew()
        elif option == "3":
            showCrew()
            id = input("Enter the identification card of the crewmember to modify:")
            name = input("Enter the name of the crewmember:")
            age = input("Enter the age of the crewmember:")
            crewAirlineMenu()
            airline = input("Enter the name of the airline which it belongs:")
            if verifyAirline(airline) == False:
                while verifyAirline(airline) == False:
                    print("This airline doesn't exist, try again")
                    airline = input("Enter the name of the airline which it belongs:")
                    if verifyAirline(airline) == True:
                        break
            type = crewRoleMenu()
            status = crewStatusMenu()
            print(modifyCrew(id, name, age, airline, type, status))

        elif option == "4":
            showCrew()
            id = input("Enter the identification card of the crewmember to delete:")
            print(deleteCrew(id))

        elif option == "5":
            mainMenu(role)

        else:
            print("Invalid option")
        crewMaintenance(role)
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the crew\n")
        print("\nMaintenance of Crew.\n",
              "1)See Crew.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showCrew()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        crewMaintenance(role)


def planeMaintenance(role):
    if role == 1:
        role = 1
        print("Aircraft Maintenance.\n",
              "1)Create Aircraft.\n",
              "2)See Aircrafts.\n",
              "3)Modify Aircraft.\n",
              "4)Delete Aircraft.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            i = 1
            while True:
                try:
                    x = int(input("Enter the number of the aircraft you are going to add:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            while i <= x:
                model = input("Enter model of the Aircraft:")
                print("Example: 2019 ")
                while True:
                    try:
                        creationYear = input("Enter the foundation year:")
                        datetime.strptime(creationYear, '%Y')
                        break
                    except:
                        print("\n You have not entered a correct year")
                id = input("Enter ID of the aircraft:")
                if verifyAircraft(id) == True:
                    while verifyAircraft(id) == True:
                        print("Aircraft already exists, try again")
                        id = input("Enter id of the Aircraft:")
                        if verifyAircraft(id) == False:
                            break
                aircraftAirlineMenu()
                airline = input("Enter the name of the airline which it belongs:")
                if verifyAirline(airline) == False:
                    while verifyAirline(airline) == False:
                        print("This airline doesn't exist, try again")
                        airline = input("Enter the name of the airline which it belongs:")
                        if verifyAirline(airline) == True:
                            break
                while True:
                    try:
                        capacity = int(input("Enter the capacity of the Aircraft:"))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
                status = aircraftStatusMenu()
                addAircraft(model, creationYear, id, airline, capacity, status)
                i = i + 1

        elif option == "2":
            showAircraft()

        elif option == "3":
            showAircraft()
            id = input("Enter the Aircraft id to modify:")
            model = input("Enter the new model year or the same:")
            print("Example: 2019 ")
            creationYear = input("Enter the creation year:")
            aircraftAirlineMenu()
            airline = input("Enter the name of the airline which it belongs:")
            if verifyAirline(airline) == False:
                while verifyAirline(airline) == False:
                    print("This airline doesn't exist, try again")
                    airline = input("Enter the name of the airline which it belongs:")
                    if verifyAirline(airline) == True:
                        break
            while True:
                try:
                    capacity = int(input("Enter the capacity of the Aircraft:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            status = aircraftStatusMenu()
            print(modifyAircraft(id, model, creationYear, airline, capacity,status))

        elif option == "4":
            showAircraft()
            id = input("Enter the ID of the aircraft to delete:")
            print(deleteAircraft(id))

        elif option == "5":
            mainMenu(role)

        else:
            print("Invalid option")
        planeMaintenance(role)
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the aircrafts\n")
        print("\nMaintenance of Aircraft.\n",
              "1)See Aircrafts.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showAircraft()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        planeMaintenance(role)


def airportMaintenance(role):
    if role == 1:
        role = 1
        print("Maintenance of Airports.\n",
              "1)Create Airports.\n",
              "2)See Airports.\n",
              "3)Modify Airports.\n",
              "4)Delete Airports.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            i = 1
            while True:
                try:
                    x = int(input("Enter the number of the airports you are going to add:"))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            while i <= x:
                name = input("Enter the name of the airport:")
                if verifyAirport(name) == True:
                    while verifyAirport(name) == True:
                        print("Airport already exists, try again")
                        name = input("Enter name of the airport:")
                        if verifyAirport(name) == False:
                            break
                city = input("Enter the name of the city where the airport is:")
                country = input("Enter the name of the country where the airport is:")
                addAirport(name, city, country)
                i = i + 1

        elif option == "2":
            showAirport()

        elif option == "3":
            showAirport()
            name = input("Enter the Airport name to modify:")
            if verifyAirport(name) == False:
                while verifyAirport(name) == False:
                    print("Airport doesn't exist, try again")
                    name = input("Enter name of the airport:")
                    if verifyAirport(name) == True:
                        break
            city = input("Enter the name of the city where the airport is:")
            country = input("Enter the name of the country where the airport is:")
            print(modifyAirport(name, city, country))

        elif option == "4":
            showAirport()
            name = input("Enter the Airport name to delete:")
            if verifyAirport(name) == False:
                while verifyAirport(name) == False:
                    print("Airport doesn't exist, try again")
                    name = input("Enter name of the airport:")
                    if verifyAirport(name) == True:
                        break
            print(deleteAirport(name))

        elif option == "5":
            mainMenu(role)

        else:
            print("Invalid option")
        airportMaintenance(role)
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the airports\n")
        print("\nMaintenance of airports.\n",
              "1)See Airports.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showAirport()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        airportMaintenance(role)


def flightMaintenance(role):
    if role == 1:
        if trackList != [] and gateList != [] and airlineList != [] and crewList != [] and airportList != []\
                and aircraftList != []:
            role = 1
            print("Maintenance of Flight.\n",
                  "1)Create Flight.\n",
                  "2)See Flight.\n",
                  "3)Modify Flight.\n",
                  "4)Delete Flight.\n",
                  "5)Back.\n")
            option = input("Enter the action you want to do:")
            if option == "1":
                crewAirlineMenu()
                airline = input("Enter the name of the airline which it belongs:")
                if verifyAirline(airline) == False:
                    while verifyAirline(airline) == False:
                        print("This airline doesn't exist, try again")
                        airline = input("Enter the name of the airline which it belongs:")
                        if verifyAirline(airline) == True:
                            break
                print("Enter the departure date below:")
                while True:
                    try:
                        departureDate = input('\n Enter the departure date ==> Example: "10/01/2000"')
                        datetime.strptime(departureDate, '%d/%m/%Y')
                        listDates.append(departureDate)
                        break
                    except:
                        print("\n You have not entered a correct date, try again")
                if verifyDepartureDate(departureDate) == False:
                    while verifyDepartureDate(departureDate) == False:
                        print("You have not entered a correct date, try again")
                        departureDate = input('\n Enter the departure date ==> Example: "10/01/2000"')
                        if verifyDepartureDate(departureDate) == True:
                            break
                while True:
                    try:
                        departureTime = input('\n Enter the departure time ==> Example: "10:30"')
                        datetime.strptime(departureTime, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct time, try again")
                while True:
                    try:
                        timeFlight = input('\n Enter the time of flight ==> Example: "2:30" ==> Its two and a half hours')
                        datetime.strptime(timeFlight, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct date")
                airportMenu()
                departureAirport = input("Enter the name of the airport which it belongs for the departure airport:")
                if verifyAirport(departureAirport) == False:
                    while verifyAirport(departureAirport) == False:
                        print("Airport doesn't exist, try again")
                        departureAirport = input("Enter the name of the airport which it belongs for the departure airport:")
                        if verifyAirport(departureAirport) == True:
                            break
                airportMenu()
                arrivalAirport = input("Enter the name of the airport which it belongs for the arrival airport:")
                if verifyAirport(arrivalAirport) == False:
                    while verifyAirport(arrivalAirport) == False:
                        print("Airport doesn't exist, try again")
                        arrivalAirport = input("Enter the name of the airport which it belongs for the arrival airport:")
                        if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                            break
                if automaticPlane() != False:
                    plane = automaticPlane()
                else:
                    print("No aircrafts available, try later")
                    flightMaintenance(role)
                if automaticGate() != False:
                    gate = automaticGate()
                else:
                    print("No gates available, try later")
                    flightMaintenance(role)
                if automaticTrack() != False:
                    track = automaticTrack()
                else:
                    print("No tracks available, try later")
                    flightMaintenance(role)
                pushListGateFlight(gate)
                pushListPlaneFlight(plane)
                automaticCrewPilots(airline)
                automaticCrewCostumerService(airline)
                price = int(input("Enter the price of the flight below"))
                if airline != None and departureDate != None and departureTime != None and timeFlight != None and\
                        departureAirport != None and arrivalAirport != None and plane != None and gate != None and\
                        track != None and price != None:
                    x = getPilots()
                    y = getCostumersServer()
                    if x != False and y != False:
                        addFlight(airline, departureDate, departureTime, timeFlight, departureAirport, arrivalAirport,
                                  plane, gate, track, x, y, price)
                        modifyStatusGate(gate, departureTime)
                        dailyFlight(departureDate)
                        if aircraftUse(departureTime, timeFlight, plane) == True:
                            flightMaintenance(role)
                        else:
                            flightMaintenance(role)
                    else:
                        print("Missing data in the crew")
                        flightMaintenance(role)
                else:
                    print("\nMissing data can not create the flight")
                    flightMaintenance(role)
                pilotsList = []
                costumersServerList = []
                gateListFlight = []
                aircraftListFlight = []
            elif option == "2":
                showFlights()

            elif option == "3":
                showFlights()
                while True:
                    try:
                        departuredate = input('\n Enter the departure date of the flight:')
                        datetime.strptime(departuredate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date")
                while True:
                    try:
                        departuretime = input('\n Enter the departure time of the flight:')
                        datetime.strptime(departuretime, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct date")
                while True:
                    try:
                        departuredate2 = input('\n Enter the new departure date of the flight:')
                        datetime.strptime(departuredate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date")
                while True:
                    try:
                        departuretime2 = input('\n Enter the new departure time of the flight:')
                        datetime.strptime(departuretime, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct date")
                while True:
                    try:
                        timeflight = input('\n Enter the new time of flight ==> Example: "2:30" ==> Its two and a half'
                                           ' hours')
                        datetime.strptime(timeflight, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct date")
                airportMenu()
                departureairport = input("Enter the name of the new airport which it belongs for the departure airport:")
                if verifyAirport(departureairport) == False:
                    while verifyAirport(departureairport) == False:
                        print("Airport doesn't exist, try again")
                        departureairport = input(
                            "Enter the name of the airport which it belongs for the departure airport:")
                        if verifyAirport(departureairport) == True:
                            break
                airportMenu()
                arrivalairport = input("Enter the correct name of the new airport which it belongs for the arrival airport:")
                if verifyAirport(arrivalairport) == False:
                    while verifyAirport(arrivalairport) == False:
                        print("Airport doesn't exist, try again")
                        arrivalairport = input("Enter the correct name of the airport which it belongs for the arrival airport:")
                        if verifyAirport(arrivalairport) == True and arrivalairport != departureairport:
                            break
                print(modifyFlight(departuredate, departuretime,departuredate2, departuretime2, timeflight, departureairport, arrivalairport))

            elif option == "4":
                showFlights()
                print("Enter the departure date of flight you want to delete below:")
                while True:
                    try:
                        departuredate = input('\n Enter the departure date of the flight to delete:')
                        datetime.strptime(departuredate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date")

                while True:
                    try:
                        departuretime = input('\n Enter the departure time of the flight to delete:')
                        datetime.strptime(departuretime, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct date")
                crewAirlineMenu()
                airline = input("Enter the name of the airline of the flight:")
                if verifyAirline(airline) == False:
                    while verifyAirline(airline) == False:
                        print("This airline doesn't exist, try again")
                        airline = input("Enter the name of the airline of the flight:")
                        if verifyAirline(airline) == True:
                            break
                automaticCrewPilots(airline)
                automaticCrewCostumerService(airline)
                getPilots()
                getCostumersServer()
                gate = input("Enter number of the gate of the flight:")
                if verifyGateFlight(gate) == False:
                    while verifyGateFlight(gate) == False:
                        print("This gate not found, try again")
                        gate = input("Enter number of the gate of the flight:")
                        if verifyGateFlight(gate) == True:
                            break
                plane = input("Enter model of the plane of the flight:")
                if verifyPlaneFlight(plane) == False:
                    while verifyPlaneFlight(plane) == False:
                        print("This plane not found, try again")
                        plane = input("Enter model of the plane of the flight:")
                        if verifyPlaneFlight(plane) == True:
                            break
                print(deleteFlight(departuredate, departuretime, gate, plane))
            elif option == "5":
                mainMenu(role)

            else:
                print("Invalid option")
            flightMaintenance(role)
        else:
            print("\nData is missing in the system to create a flight\n")
    else:
        role = 2
        print("\nYou are in guest mode, You can only see the flights\n")
        print("\nMaintenance of flights.\n",
              "1)See flights.\n",
              "2)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            showFlights()
        elif option == "2":
            mainMenu(role)
        else:
            print("Invalid option")
        flightMaintenance(role)

def reports(role):
    if role == 1:
        if trackList != [] and gateList != [] and airlineList != [] and crewList != [] and airportList != [] \
                and aircraftList != []:
            role = 1
            print("\nReports\n",
                  "1)See the list of flights made in a range of dates.\n",
                  "2)See the list of flights made at a boarding gate.\n",
                  "3)See the ranking of airports with the most registered flights.\n",
                  "4)See the ranking of crew members with the most flights made.\n",
                  "5)Back.\n")
            option = input("Enter the action you want to do:")

            if option == "1":
                while True:
                    try:
                        firstDate = input('\n Enter the first date,remember that the first date must be less than the '
                                          'second:')
                        datetime.strptime(firstDate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date, try again")
                while True:
                    try:
                        secondDate = input('\n Enter the second date,remember that the second date must be greater '
                                           'than the first')
                        datetime.strptime(secondDate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date, try again")
                if verifyDates(firstDate, secondDate) == False:
                    while verifyDates(firstDate, secondDate)== False:
                        print("Incorrect dates, try again")
                        while True:
                            try:
                                firstDate = input(
                                    '\n Enter the first date,remember that the first date must be less than the '
                                    'second:')
                                datetime.strptime(firstDate, '%d/%m/%Y')
                                break
                            except:
                                print("\n You have not entered a correct date, try again")
                        while True:
                            try:
                                secondDate = input(
                                    '\n Enter the second date,remember that the second date must be greater '
                                    'than the first' )
                                datetime.strptime(secondDate, '%d/%m/%Y')
                                break
                            except:
                                print("\n You have not entered a correct date, try again")
                        if verifyDates(firstDate, secondDate) == True:
                            break
                firstReport(firstDate, secondDate)
            elif option == "2":
                gate = input("Enter number of the gate of the flight:")
                if verifyGateFlight(gate) == False:
                    while verifyGateFlight(gate) == False:
                        print("This gate not found, try again")
                        gate = input("Enter number of the gate of the flight:")
                        if verifyGateFlight(gate) == True:
                            break
                secondReport(gate)

            elif option == "3":
                thirdReport()

            elif option == "4":
                fourthReport()
            elif option == "5":
                mainMenu(role)
            else:
                print("Invalid option")
            reports(role)
    elif role == 2:
        print("\nYou are in guest mode\n")
        print("\nReports.\n",
              "1)See the list of flights made in a range of dates.\n",
              "2)See the list of flights made at a boarding gate.\n",
              "3)See the ranking of airports with the most registered flights.\n",
              "4)See the ranking of crew members with the most flights made.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            while True:
                try:
                    firstDate = input('\n Enter the first date,remember that the first date must be less than the '
                                      'second:')
                    datetime.strptime(firstDate, '%d/%m/%Y')
                    break
                except:
                    print("\n You have not entered a correct date, try again")
            while True:
                try:
                    secondDate = input('\n Enter the second date,remember that the second date must be greater '
                                       'than the first')
                    datetime.strptime(secondDate, '%d/%m/%Y')
                    break
                except:
                    print("\n You have not entered a correct date, try again")
            if verifyDates(firstDate, secondDate) == False:
                while verifyDates(firstDate, secondDate) == False:
                    print("Incorrect dates, try again")
                    while True:
                        try:
                            firstDate = input(
                                '\n Enter the first date,remember that the first date must be less than the '
                                'second:')
                            datetime.strptime(firstDate, '%d/%m/%Y')
                            break
                        except:
                            print("\n You have not entered a correct date, try again")
                    while True:
                        try:
                            secondDate = input(
                                '\n Enter the second date,remember that the second date must be greater '
                                'than the first')
                            datetime.strptime(secondDate, '%d/%m/%Y')
                            break
                        except:
                            print("\n You have not entered a correct date, try again")
                    if verifyDates(firstDate, secondDate) == True:
                        break
            firstReport(firstDate, secondDate)

        elif option == "2":
            gate = input("Enter number of the gate of the flight:")
            if verifyGateFlight(gate) == False:
                while verifyGateFlight(gate) == False:
                    print("This gate not found, try again")
                    gate = input("Enter number of the gate of the flight:")
                    if verifyGateFlight(gate) == True:
                        break
            secondReport(gate)
        elif option == "3":
            thirdReport()
        elif option == "4":
            fourthReport()
        elif option == "5":
            mainMenu(role)
        else:
            print("Invalid option")
        reports(role)
    elif role == 3:
        print("\nYou are in passenger mode\n")
        print("\nReports.\n",
              "1)See the list of flights made in a range of dates.\n",
              "2)See the list of flights made at a boarding gate.\n",
              "3)See the ranking of airports with the most registered flights.\n",
              "4)See the ranking of crew members with the most flights made.\n",
              "5)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            while True:
                try:
                    firstDate = input('\n Enter the first date,remember that the first date must be less than the '
                                      'second:')
                    datetime.strptime(firstDate, '%d/%m/%Y')
                    break
                except:
                    print("\n You have not entered a correct date, try again")
            while True:
                try:
                    secondDate = input('\n Enter the second date,remember that the second date must be greater '
                                       'than the first')
                    datetime.strptime(secondDate, '%d/%m/%Y')
                    break
                except:
                    print("\n You have not entered a correct date, try again")
            if verifyDates(firstDate, secondDate) == False:
                while verifyDates(firstDate, secondDate) == False:
                    print("Incorrect dates, try again")
                    while True:
                        try:
                            firstDate = input(
                                '\n Enter the first date,remember that the first date must be less than the '
                                'second:')
                            datetime.strptime(firstDate, '%d/%m/%Y')
                            break
                        except:
                            print("\n You have not entered a correct date, try again")
                    while True:
                        try:
                            secondDate = input(
                                '\n Enter the second date,remember that the second date must be greater '
                                'than the first')
                            datetime.strptime(secondDate, '%d/%m/%Y')
                            break
                        except:
                            print("\n You have not entered a correct date, try again")
                    if verifyDates(firstDate, secondDate) == True:
                        break
            firstReport(firstDate, secondDate)

        elif option == "2":
            gate = input("Enter number of the gate of the flight:")
            if verifyGateFlight(gate) == False:
                while verifyGateFlight(gate) == False:
                    print("This gate not found, try again")
                    gate = input("Enter number of the gate of the flight:")
                    if verifyGateFlight(gate) == True:
                        break
            secondReport(gate)
        elif option == "3":
            thirdReport()
        elif option == "4":
            fourthReport()
        elif option == "5":
            mainMenu(role)
        else:
            print("Invalid option")
        reports(role)

def flights(role):
    return

def passengerMenu(role):
    if role == 3:
        role = 3
        print("\nYou are in passenger mode\n"
              "\nAero-TEC\n",
              "1)Flights.\n",
              "2)Log out.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            flights(role)
        elif option == "2":
            loginMenu()
        else:
            print("Invalid option")
        passengerMenu(role)
def mainMenu(role):
    if role == 1:
        role = 1
        print("\nYou are in admin mode\n"
              "\nAero-TEC\n",
              "1)Maintenance of tracks.\n",
              "2)Maintenance of doors of boarding.\n",
              "3)Airline maintenance.\n",
              "4)Crew maintenance\n",
              "5)Aircraft maintenance.\n",
              "6)Airport maintenance.\n",
              "7)Flight maintenance.\n",
              "8)Reports.\n",
              "9)Log out\n")
        option = input("Enter the action you want to do:")

        if option == "1":
            maintenanceTracks(role)
        elif option == "2":
            maintenanceGates(role)

        elif option == "3":
            airlineMaintenance(role)

        elif option == "4":
            crewMaintenance(role)

        elif option == "5":
            planeMaintenance(role)

        elif option == "6":
            airportMaintenance(role)

        elif option == "7":
            flightMaintenance(role)

        elif option == "8":
            reports(role)

        elif option == "9":
            loginMenu()
        else:
            print("Invalid option")
        mainMenu(role)
    elif role == 2:
        print("\nYou are in guest mode, Only read\n"
                "\nAero-TEC\n",
                "1)Flights.\n",
                "2)Reports.\n",
                "3)Log out\n")
        option = input("Enter the action you want to do:")

        if option == "1":
            flightMaintenance(role)

        elif option == "2":
            reports(role)

        elif option == "3":
             loginMenu()

        else:
            print("Invalid option")
        mainMenu(role)

    elif role == 3:
        print("\nYou are in passenger mode\n"
              "\nAero-TEC\n",
              "1)Maintenance of tracks.\n",
              "2)Maintenance of doors of boarding.\n",
              "3)Airline maintenance.\n",
              "4)Crew maintenance\n",
              "5)Aircraft maintenance.\n",
              "6)Airport maintenance.\n",
              "7)Flight maintenance.\n",
              "8)Reports.\n",
              "9)Log out\n")
        option = input("Enter the action you want to do:")

        if option == "1":
            maintenanceTracks(role)

        elif option == "2":
            maintenanceGates(role)

        elif option == "3":
            airlineMaintenance(role)

        elif option == "4":
            crewMaintenance(role)

        elif option == "5":
            planeMaintenance(role)

        elif option == "6":
            airportMaintenance(role)

        elif option == "7":
            flightMaintenance(role)

        elif option == "8":
            reports(role)

        elif option == "9":
            loginMenu()
        else:
            print("Invalid option")
        mainMenu(role)



def loginMenu():
    print("Aero-TEC\n",
          "1)Log in.\n",
          "2)Sign up.\n",
          "3)Show Info.\n" )
    option = input("Enter the action you want to do:")

    if option == "1":
        id = input("Enter id:")
        password = input("Enter password:")
        role = logIn(id, password)
        if role == 1:
            mainMenu(role)
        elif role == 2:
            mainMenu(role)
        elif role == 3:
            passengerMenu(role)
        else:
            print(role)

    elif option == "2":
        name = input("Enter name:")
        while True:
            try:
                age = int(input("Enter age:"))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        email = input("Enter email:")
        if verifyEmail(email) == True:
            while verifyEmail(email) == True:
                print("Email already exists, try again")
                email = input("Enter email:")
                if verifyEmail(email) == False:
                    break
        id = input("Enter identification card:")
        if verifyID(id) == True:
            while verifyID(id) == True:
                print("ID already exists, try again")
                id = input("Enter id:")
                if verifyID(id) == False:
                    break
        password = input("Enter password:")
        while True:
            try:
                role = int(input("Enter 1 to admin or 2 to guest or 3 to passenger:"))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if role != 1 and role != 2 and role != 3:
            while role != 1 and role != 2 and role != 3:
                print("Error please enter 1 or 2 or 3")
                role = int(input("Enter 1 to admin or 2 to guest or 3 for passenger"))
                if role == 1 or role == 2 or role == 3:
                    break
        addUser(name, age, email, id, password, role)

    elif option == "3":
        showInfoUser()
    else:
        print("Invalid option")
    loginMenu()


def start():
    global flightList
    flightList = charge()
    loginMenu()

start()

