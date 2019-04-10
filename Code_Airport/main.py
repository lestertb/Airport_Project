from User import *
from TrackMaintenance import *
from GateMaintenance import *
from random import random

usersList = []
trackList = []
gateList = []
crewList = []
airportList = []


'------------------------------------------#Fuctions---------------------------------------'


def addUser(name, age, email, id, password, role):
    newUser = User(name, age, email, id, password, role)
    usersList.append(newUser)


def showInfoUser():
    if usersList != []:
        for user in usersList:
            print("Name: ", user.name, "Age: ", user.age,
                  "Email: ", user.email, "ID: ", user.id,
                  "Password:", user.password, "Role:", user.role)
    else:
        print("\nNo users found\n")

def verifyID(id):
    for user in usersList:
        if id == user.id:
            return True
        else:
            return False

def verifyEmail(email):
    for user in usersList:
        if email == user.email:
            return True
        else:
            return False


def logIn(id, password):
    while usersList != []:
        for user in usersList:
            if user.id == id and user.password == password:
                role = user.role
                if role == 1:
                    return role
                else:
                    return role
            else:
                return "\n User not found, Please Sign up\n"
    return "\n User not found, Please Sign up\n"

def addTrack(number, status):
    newTrack = MaintenenceTracks(number, status)
    trackList.append(newTrack)

def verifyTrack(number):
    for track in trackList:
        if number == track.number:
            return True
        else:
            return False

def showTracks():
    if trackList != []:
        for track in trackList:
            print("Track Number: ", track.number, "Stat: ", track.status)
    else:
        print("\nNo tracks found\n")

def modifyTrack(number,status):
    for track in trackList:
        if number == track.number:
            track.status = status
            return "\nSuccessful modification\n"
        else:
            return "\nTrack no found\n"

def deleteTrack(number):
    for track in trackList:
        if number == track.number:
            trackList.remove(track)
            return "\nSuccessful delete\n"
        else:
            return "\nTrack no found\n"

def addGate(number, status):
    newGate = MaintenanceGates(number, status)
    gateList.append(newGate)

def verifyGate(number):
    for gate in gateList:
        if number == gate.number:
            return True
        else:
            return False

def showGates():
    if gateList != []:
     for gate in gateList:
         print("Gate number:",gate.number, "Gate status:", gate.status)
     else:
         print("\nNo gates found\n")

def modifyGate(number,status):
    for gate in gateList:
        if number == gate.number:
            gate.status = status
            return "\nSuccessful modification\n"
        else:
            return "\nGate no found\n"
def addGateByNumber(num):
    i = 1
    while i < num:
        for _ in range(num):
            value = random()
            newGate = MaintenanceGates(value, "Available")
            gateList.append(newGate)
        i += 1

def deleteGate(number):
    if gateList != []:
        for gate in gateList:
            if number == gate.number:
                gateList.remove(gate)
                return "\nSuccesful delete\n"
            else:
                return "\nGate not found\n"

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
            x = int(input("Enter the number of tracks you are going to add:"))
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
            return
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
            return
        maintenanceTracks(role)

def maintenanceGates(role):
    if role == 1:
        role = 1
        print("Maintenance of boarding gates.\n",
              "1)Create Gates.\n",
              "2)See Gates.\n",
              "3)Modify Gates.\n",
              "4)Delete Gates.\n",
              "5)Add Gates by cuantity.\n",
              "6)Back.\n")
        option = int(input("Enter the action you want to do:"))
        if option == "1":
            i = 1
            x = int(input("Enter the number of tracks you are going to add:"))
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
            num = int(input("Enter the number of gates you want to add:"))
            addGateByNumber(num)
        elif option == "6":
            mainMenu(role)
        else:
            return maintenanceGates(role)
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
            return
        maintenanceGates(role)


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


def mainMenu(role):
    if role == 1:
        print("\nYou are in admin mode\n"
              "\nAero-TEC\n",
              "1)Maintenance of tracks.\n",
              "2)Maintenance of doors of boarding.\n",
              "3)Airline maintenance.\n",
              "4)Crew maintenance\n",
              "5)Aircraft maintenance.\n",
              "6)Airport maintenance.\n",
              "7)Flight maintenance.\n",
              "8)Log out\n")
        option = input("Enter the action you want to do:")

        if option == "1":
            role = 1
            maintenanceTracks(role)
        elif option == "2":
            role = 1
            maintenanceGates(role)

        elif option == "8":
            loginMenu()

        else:
            return
    else:
        print("\nYou are in guest mode, Only read\n"
              "\nAero-TEC\n",
              "1)Maintenance of tracks.\n",
              "2)Maintenance of doors of boarding.\n",
              "3)Airline maintenance.\n",
              "4)Crew maintenance\n",
              "5)Aircraft maintenance.\n",
              "6)Airport maintenance.\n",
              "7)Flight maintenance.\n",
              "8)Log out\n")
        option = input("Enter the action you want to do:")

        if option == "1":
            role = 2
            maintenanceTracks(role)

        elif option == "8":
            loginMenu()

        else:
            return

def loginMenu():
    print("Aero-TEC\n",
          "1)Log in.\n",
          "2)Sign up.\n",
          "3)Show Info.\n")
    option = input("Enter the action you want to do:")

    if option == "1":
        id = input("Enter id:")
        password = input("Enter password:")
        role = logIn(id, password)
        if role == 1:
            mainMenu(role)
        elif role == 2:
            mainMenu(role)
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
        role = int(input("Enter 1 to admin or 2 to guest:"))
        if role != 1 and role != 2:
            while role != 1 and role != 2:
                print("Error please enter 1 or 2")
                role = int(input("Enter 1 to admin or 2 to guest:"))
                if role == 1 or role == 2:
                    break
        addUser(name, age, email, id, password, role)

    elif option == "3":
        showInfoUser()

    else:
        print("Invalid option")
        return
    loginMenu()
loginMenu()




