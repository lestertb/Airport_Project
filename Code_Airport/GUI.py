from main import *
from tkinter import *
from tkinter import ttk


def login2():
    for user in usersList:
        if user.id == entryID.get() and user.password == entryPassword.get() and user.role == 3:
            choose()

    else:
        return


def choose():
    root.withdraw()
    window1 = Toplevel(bg="#D2F1A9", width=550, height=400)
    x = 200
    y = 200
    window1.geometry('+%d+%d' % (x, y))
    window1.title("Flight Searching")
    window1.iconbitmap("plane.ico")
    window1.resizable(False, False)

    def v2():
        window1.destroy()
        root.deiconify()

    def hide():
        window1.destroy()
        windowSearch()

    def create():
        window1.destroy()
        createFlight2()

    buttonS = Button(window1, text="Flight Searching", bg="lightgreen", font=20, command=hide)
    buttonS.place(rely=0, relx=0, relwidth=0.5, relheight=0.9)

    buttonT = Button(window1, text="Create Trip", bg="lightgreen", font=20, command=create)
    buttonT.place(rely=0, relx=0.5, relwidth=0.5, relheight=0.9)

    buttonW = Button(window1, text="Return", bg="lightblue", font=20, command=v2)
    buttonW.place(rely=0.9, relx=0, relwidth=1, relheight=0.1)


def windowSearch():
    root.withdraw()

    window = Toplevel(bg="#D2F1A9", width=550, height=400)
    x = 200
    y = 200
    window.geometry('+%d+%d' % (x, y))
    window.title("Flight Searching")
    window.iconbitmap("plane.ico")
    window.resizable(False, False)

    def v3():
        window.destroy()
        windowSearch()

    fr2 = Frame(window, bg="white")
    fr2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    label2 = Label(fr2, text="Flight Searching", bg="white", font=("Arial", 20))
    label2.pack()

    departureLabel = Label(fr2, text="Departure Airport: ", bg="white", font=("Arial", 14))
    departureLabel.place(rely=0.20)

    arrivalLabel = Label(fr2, text="Arrival Airport: ", bg="white", font=("Arial", 14))
    arrivalLabel.place(rely=0.40)

    dat = Label(fr2, text="Insert the date: ", bg="white", font=("Arial", 14))
    dat.place(rely=0.60)

    wayLabel = Label(fr2, text="Search only: ", bg="white", font=("Arial", 14))
    wayLabel.place(rely=0.80)

    way = ttk.Combobox(fr2, values=["one way", "round trip"])
    way.place(rely=0.82, relx=0.5, relwidth=0.45)

    departureCombo = ttk.Combobox(fr2, values=["Juan SantaMaria Airport", "Jamaica Airport", "Panama Airport",
                                               "Tacos Airport", "Bogota Airport", "Canada Airport", "Texas Airport"
        , "Managua Airport", "Ecuador Airport", "Brasilia Airport", "Buenos Aires Airport", "Barcelona Airport",
                                               "Russia Airport", "Italy Airport", "Peru Airport", "Venezuela Airport",
                                               "Honduras Airport", "Uruguay Airport",
                                               "Haiti Airport", "Guatemala Airport", "Chile Airport", "Cuba Airport",
                                               "Bolivia Airport"])
    departureCombo.place(rely=0.20, relx=0.5, relwidth=0.45)

    arrivalCombo = ttk.Combobox(fr2, values=["Juan SantaMaria Airport", "Jamaica Airport", "Panama Airport",
                                             "Tacos Airport", "Bogota Airport", "Canada Airport", "Texas Airport"
        , "Managua Airport", "Ecuador Airport", "Brasilia Airport", "Buenos Aires Airport", "Barcelona Airport",
                                             "Russia Airport", "Italy Airport", "Peru Airport", "Venezuela Airport",
                                             "Honduras Airport", "Uruguay Airport",
                                             "Haiti Airport", "Guatemala Airport", "Chile Airport", "Cuba Airport",
                                             "Bolivia Airport"])
    arrivalCombo.place(rely=0.40, relx=0.5, relwidth=0.45)



    dayEntry = Entry(fr2)
    dayEntry.place(rely=0.6, relx=0.5, relwidth=0.1)

    monthEntry = Entry(fr2)
    monthEntry.place(rely=0.6, relx=0.65, relwidth=0.1)

    yearEntry = Entry(fr2)
    yearEntry.place(rely=0.6, relx=0.8, relwidth=0.1)

    list = []

    def search2():
        dat = (dayEntry.get() + "/" + monthEntry.get() + "/" + yearEntry.get())

        if way.get() == "one way":
            for Flight in flightList:

                # if way.get() == Flight.trip:
                if departureCombo.get() == Flight.departureAirport and arrivalCombo.get() == Flight.arrivalAirport:
                    x = Flight.departureDate

                    datetime.strptime(x, '%d/%m/%Y')
                    datetime.strptime(dat, '%d/%m/%Y')
                    if dat == x:
                        print("\n", "Flight:\n",
                              "The airline is:", Flight.airline, "\n",
                              "Departure Date:", Flight.departureDate, "\n",
                              "Departure Time:", Flight.departureTime, "\n",
                              "Flight time:", Flight.timeFlight, "\n",
                              "Departure airport:", Flight.departureAirport, "\n",
                              "Arrival airport:", Flight.arrivalAirport, "\n",
                              "Airplane ID:", Flight.plane, "\n",
                              "Door number:", Flight.gate, "\n",
                              "Track number:", Flight.track, "\n",
                              "Crew of pilots:", Flight.crewPilot, "\n",
                              "Crew of costumer services:", Flight.crewCustomerService, "\n",
                              "The price is:", Flight.price, "\n")
                        list.append(Flight)

        elif way.get() == "round trip":
            for Flight in registerList:
                # if way.get() == Flight.trip:
                if departureCombo.get() == Flight.departureAirport and arrivalCombo.get() == Flight.arrivalAirport:
                    x = Flight.departureDate
                    datetime.strptime(x, '%d/%m/%Y')
                    datetime.strptime(dat, '%d/%m/%Y')
                    if dat == x:
                        print("\n", "Vuelo:\n",
                              "The airline is:", Flight.airline, "\n",
                              "Departure Date:", Flight.departureDate, "\n",
                              "Departure Time:", Flight.departureTime, "\n",
                              "Flight time:", Flight.timeFlight, "\n",
                              "Departure airport:", Flight.departureAirport, "\n",
                              "Arrival airport:", Flight.arrivalAirport, "\n",
                              "Airplane ID:", Flight.plane, "\n",
                              "Door number:", Flight.gate, "\n",
                              "Track number:", Flight.track, "\n",
                              "Crew of pilots:", Flight.crewPilot, "\n",
                              "Crew of costumer services:", Flight.crewCustomerService, "\n",
                              "The price is:", Flight.price, "\n")
                        list.append(Flight)

        else:
            print("Not available flights...")

    def v2():
        choose()
        window.destroy()

    def jmm2():
        search2()
        listFlights = Listbox(window)
        listFlights.place(rely=0, relx=0, relwidth=1, relheight=1)

        num = 1
        for Flight in list:
            listFlights.insert(1, "Flights found:",
                               str(num) + "-Flight:",
                               "The airline is:", Flight.airline, "\n",
                               "Departure Date:", Flight.departureDate, "\n",
                               "Departure Time:", Flight.departureTime, "\n",
                               "Flight time:", Flight.timeFlight, "\n",
                               "Departure airport:", Flight.departureAirport, "\n",
                               "Arrival airport:", Flight.arrivalAirport, "\n",
                               "Airplane ID:", Flight.plane, "\n",
                               "Door number:", Flight.gate, "\n",
                               "Track number:", Flight.track, "\n",
                               "Crew of pilots:", Flight.crewPilot, "\n",
                               "Crew of costumer services:", Flight.crewCustomerService, "\n",
                               "The price is:", Flight.price, "\n")
            num = num + 1

        button2 = Button(window, text="Return", bg="lightgrey", command=v3)
        button2.place(rely=0.9, relx=0, relwidth=1, relheight=0.1)

    button = Button(window, text="Search", bg="lightgrey", command=jmm2)
    button.place(rely=0.88, relx=0.57, relwidth=0.1, relheight=0.09)

    button2 = Button(window, text="Return", bg="lightgrey", command=v2)
    button2.place(rely=0.88, relx=0.33, relwidth=0.1, relheight=0.09)


def createFlight2():
    # newTravel = history(departure, arrival, scale, duration, passenger, flights)

    window2 = Toplevel(bg="#D2F1A9", width=550, height=400)
    x = 200
    y = 200
    window2.geometry('+%d+%d' % (x, y))
    window2.title("Create Flight")
    window2.iconbitmap("plane.ico")
    window2.resizable(False, False)

    def v6():
        choose()
        window2.destroy()

    fr3 = Frame(window2, bg="white")
    fr3.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    label2 = Label(fr3, text="Create", bg="white", font=("Arial", 20))
    label2.pack()

    departureLabel = Label(fr3, text="Airport departure: ", bg="white", font=("Arial", 14))
    departureLabel.place(rely=0.20)

    arrivalLabel = Label(fr3, text="Airport arrival: ", bg="white", font=("Arial", 14))
    arrivalLabel.place(rely=0.30)
    departureCombo = ttk.Combobox(fr3, values=["Juan SantaMaria Airport", "Jamaica Airport", "Panama Airport",
                                               "Tacos Airport", "Bogota Airport", "Canada Airport", "Texas Airport"
        , "Managua Airport", "Ecuador Airport", "Brasilia Airport", "Buenos Aires Airport", "Barcelona Airport",
                                               "Russia Airport", "Italy Airport", "Peru Airport", "Venezuela Airport",
                                               "Honduras Airport", "Uruguay Airport",
                                               "Haiti Airport", "Guatemala Airport", "Chile Airport", "Cuba Airport",
                                               "Bolivia Airport"])
    departureCombo.place(rely=0.20, relx=0.5, relwidth=0.45)

    arrivalCombo = ttk.Combobox(fr3, values=["Juan SantaMaria Airport", "Jamaica Airport", "Panama Airport",
                                             "Tacos Airport", "Bogota Airport", "Canada Airport", "Texas Airport"
        , "Managua Airport", "Ecuador Airport", "Brasilia Airport", "Buenos Aires Airport", "Barcelona Airport",
                                             "Russia Airport", "Italy Airport", "Peru Airport", "Venezuela Airport",
                                             "Honduras Airport", "Uruguay Airport",
                                             "Haiti Airport", "Guatemala Airport", "Chile Airport", "Cuba Airport",
                                             "Bolivia Airport"])
    arrivalCombo.place(rely=0.32, relx=0.5, relwidth=0.45)

    scaleLabel = Label(fr3, text="Scale(1 for yes or 0 for no): ", bg="white", font=("Arial", 14))
    scaleLabel.place(rely=0.40)
    scaleCombo = ttk.Combobox(fr3, values=[1, 0])
    scaleCombo.place(rely=0.42, relx=0.5, relwidth=0.45)

    duration = Label(fr3, text="Insert the duration of the trip\n(4 = 4:00h): ", bg="white", font=("Arial", 14))
    duration.place(rely=0.52)

    hourEntry = Entry(fr3)
    hourEntry.place(rely=0.56, relx=0.6, relwidth=0.344)

    name1 = Label(fr3, text="Insert the name of the passenger: ", bg="white", font=("Arial", 14))
    name1.place(rely=0.70)

    entryName = Entry(fr3)
    entryName.place(rely=0.7, relx=0.6, relwidth=0.344)

    def createTravel():
        departure = departureCombo.get()
        arrival = arrivalCombo.get()
        departureT = (hourEntry.get() + ":00")

        passenger = entryName.get()

        scale = ""
        duration = "1"
        duration = datetime.strptime(duration, '%H')
        flights = []
        var = ""

        for Flight in flightList:
            if departure == Flight.departureAirport and arrival == Flight.arrivalAirport:
                x = Flight.departureTime
                datetime.strptime(x, '%H:%M')
                datetime.strptime(departureT, '%H:%M')
                print(departureT, x)
                if departureT == x:
                    #print(departureT, x)
                    flights.append(
                        "Airline:" + Flight.airline + " -DepartureDate: " + Flight.departureDate + " -DepartureTime: " + Flight.departureTime + " -Duration: " + Flight.timeFlight
                        + " -DepartureAirport: " + Flight.departureAirport + " -ArrivalAirport: " + Flight.arrivalAirport + " -Airplane: " + Flight.plane + " -Gate: " + Flight.gate
                        + " -Track: " + Flight.track + " -Pilots: " + Flight.crewPilot + " -CostumersCrew: " + Flight.crewCustomerServicestumer
                        + " -Price: " + Flight.price)

                    duration = Flight.timeFlight
                    var = True

        if var == True:
            newTravel = Travel(departure, arrival, scale, duration, passenger)
            travelList.append(newTravel)
            recordList.appende(newTravel)

        else:
            print("error")

    def final():
        createTravel()
        saveRecord(recordList)

    button4 = Button(window2, text="Create", bg="lightgrey", command=final)
    button4.place(rely=0.90, relx=0.57, relwidth=0.2, relheight=0.09)

    button5 = Button(window2, text="Return", bg="lightgrey", command=v6)
    button5.place(rely=0.90, relx=0.30, relwidth=0.2, relheight=0.09)


root = Tk()
root.title("AEROTEC")
root.iconbitmap("plane.ico")
root.resizable(False, False)

x = 200
y = 200
root.geometry('+%d+%d' % (x, y))

canvas = Canvas(bg="#D2F1A9", width=550, height=400)
canvas.pack()

fr = Frame(root, bg="white")
fr.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

fr.config(bg="white")

label = Label(fr, text="Login", bg="white", font=("Arial", 20))
label.pack()

labelID = Label(fr, text="Insert yout ID: ", bg="white", font=("Arial", 14))
labelID.place(rely=0.20)

passwordLabel = Label(fr, text="Insert your password: ", bg="white", font=("Arial", 14))
passwordLabel.place(rely=0.40)

entryID = Entry(fr, font=12)
entryID.place(rely=0.20, relx=0.5, relwidth=0.45)

entryPassword = Entry(fr, font=12)
entryPassword.place(rely=0.40, relx=0.5, relwidth=0.45)

button = Button(fr, text="Log In", bg="lightgrey", command=login2)
button.place(rely=0.90, relx=0.57, relwidth=0.2, relheight=0.09)

button2 = Button(fr, text="Quit", bg="lightgrey", command=root.destroy)
button2.place(rely=0.90, relx=0.33, relwidth=0.2, relheight=0.09)

root.mainloop()
