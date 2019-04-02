class User:
    def __init__(self,name, age, email,id , password, role):
        self.name = name
        self.age = age
        self.email = email
        self.id = id
        self.password = password
        self.role = role
        self.adminList = []
        self.guestList = []

    def addAdmin(self, admin):
        self.adminList.append(admin)



    def addGuest(self, guest):
        self.guestList.append(guest)
