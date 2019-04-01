class Users:
    def __init__(self,name, age, email, password,id, role):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.id = id
        self.role = role
        self.adminList = []
        self.guestList = []

    def addAdmin(self, admin):
        self.adminList.append(admin)



    def addGuest(self, guest):
        self.guestList.append(guest)
