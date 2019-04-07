from User import *
from Admin import *
from Guest import *
import getpass
import os

usersList = []
trackList = []

def addUser(name, age, email, id, password, role):
    newUser = User(name, age, email, id, password, role)
    usersList.append(newUser)

def addAdmin(name, id, password):
    for user in usersList:
        if user.name == name:
            newAdmin = Admin(id,password)
            user.addAdmin(newAdmin)


def showInfoUser():
    for user in usersList:
        print("Name: ", user.name, "Age: ", user.age, "Email: ", user.email,
              "Password", "ID: ", user.id, "Role:", user.role)


def logIn(id, password):
    if usersList == []:
        return "User not found"
    else:
        for user in usersList:
            if user.id == id and user.password == password:
               for admin in user.adminList:
                   if admin.id == id and admin.password == password:
                       role = 1
                       return role
            else:
                return "User not found"

def addTracks (number, state):
    trackList.append(number, state)
    


def maintenanceTracks ():
    print("Maintenence of Tracks.\n",
          "1)Create Tracks.\n",
          "2)See Tracks.\n",
          "3)Modify Tracks.\n",
          "4)Eliminate Tracks.")
    option = int(input("Enter the action you want to do:"))
    if option == "1":
        number =input("Enter number of the track:")
        state =input("Enter state of track:")
        addTracks(number,state)




def Menu():
    print("Aero-TEC\n",
          "1)Log in.\n",
          "2)Sign up.\n",)
    option = input("Enter the action you want to do:")

    if option == "1":
        id = input("Enter id:")
        password = input("Enter password:")
        print(logIn(id, password))

    elif option == "2":
        name = input("Enter name:")
        age = int(input("Enter age:"))
        email = input("Enter email:")
        password = getpass.getpass("Enter password:")
        id = input("Enter identification card:")
        role = int(input("Enter 1 to admin or 2 to guest:"))
        if role == 1:
            addAdmin(name, id, password)
        addUser(name, age, email, id, password, role)
    else:
        "Invalid option"
        return
    Menu()
Menu()


def mainMenu():
    print("Aero-TEC\n",
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
        maintenanceTracks()


    else:
        return

