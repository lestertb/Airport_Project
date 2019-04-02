from User import *
from Admin import *
from Guest import *
import getpass
import os

usersList = []

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
    print("hola1")
    if usersList == []:
        return "User not found"
    else:
        print("hola2")
        for user in usersList:
            print("hola3")
            if user.id == id and user.password == password:
               print("hola4")
               for admin in user.adminList:
                   print("hola5")
                   if admin.id == id and admin.password == password:
                       print("hola6")
                       role = 1
                       return role
            else:
                return "User not found"



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
        return

    else:
        return