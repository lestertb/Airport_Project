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
from Travel import *
from Record import *
from collections import Counter
import random
import sys

'------------------------------------------#Lists---------------------------------------'

# Declaration of global lists
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
flightListFilter = []
travelList = []
recordList = []

# Data to inject
userTest = User("lester", 18, "lestertb", "123", "111", 1)
usersList.append(userTest)

userTest1 = User("lestertb", 18, "lester", "1234", "1111", 3)
usersList.append(userTest1)

trackTest1 = MaintenenceTracks("10", "Available")
trackList.append(trackTest1)

trackTest2 = MaintenenceTracks("12", "Available")
trackList.append(trackTest2)

trackTest3 = MaintenenceTracks("13", "Available")
trackList.append(trackTest3)

trackTest4 = MaintenenceTracks("14", "Available")
trackList.append(trackTest4)

trackTest5 = MaintenenceTracks("15", "Available")
trackList.append(trackTest5)

trackTest6 = MaintenenceTracks("16", "Available")
trackList.append(trackTest6)

trackTest7 = MaintenenceTracks("17", "Available")
trackList.append(trackTest7)

trackTest8 = MaintenenceTracks("18", "Available")
trackList.append(trackTest8)

trackTest9 = MaintenenceTracks("19", "Available")
trackList.append(trackTest9)

trackTest10 = MaintenenceTracks("20", "Available")
trackList.append(trackTest10)

trackTest11 = MaintenenceTracks("21", "Available")
trackList.append(trackTest11)

trackTest12 = MaintenenceTracks("22", "Available")
trackList.append(trackTest12)

trackTest13 = MaintenenceTracks("23", "Available")
trackList.append(trackTest13)

trackTest14 = MaintenenceTracks("24", "Available")
trackList.append(trackTest14)

trackTest15 = MaintenenceTracks("25", "Available")
trackList.append(trackTest15)

trackTest16 = MaintenenceTracks("26", "Available")
trackList.append(trackTest16)

trackTest17 = MaintenenceTracks("27", "Available")
trackList.append(trackTest17)

trackTest18 = MaintenenceTracks("28", "Available")
trackList.append(trackTest18)

trackTest19 = MaintenenceTracks("29", "Available")
trackList.append(trackTest19)

trackTest20 = MaintenenceTracks("30", "Available")
trackList.append(trackTest20)

trackTest21 = MaintenenceTracks("31", "Available")
trackList.append(trackTest21)

trackTest22 = MaintenenceTracks("32", "Available")
trackList.append(trackTest22)

trackTest23 = MaintenenceTracks("33", "Available")
trackList.append(trackTest23)

trackTest24 = MaintenenceTracks("34", "Available")
trackList.append(trackTest24)

trackTest25 = MaintenenceTracks("35", "Available")
trackList.append(trackTest25)

trackTest26 = MaintenenceTracks("36", "Available")
trackList.append(trackTest26)

trackTest27 = MaintenenceTracks("37", "Available")
trackList.append(trackTest27)

trackTest28 = MaintenenceTracks("38", "Available")
trackList.append(trackTest28)

trackTest29 = MaintenenceTracks("39", "Available")
trackList.append(trackTest29)

trackTest30 = MaintenenceTracks("40", "Available")
trackList.append(trackTest30)

trackTest31 = MaintenenceTracks("41", "Available")
trackList.append(trackTest31)

trackTest32 = MaintenenceTracks("42", "Available")
trackList.append(trackTest32)

trackTest33 = MaintenenceTracks("43", "Available")
trackList.append(trackTest33)

trackTest34 = MaintenenceTracks("44", "Available")
trackList.append(trackTest34)

trackTest35 = MaintenenceTracks("45", "Available")
trackList.append(trackTest35)

trackTest36 = MaintenenceTracks("46", "Available")
trackList.append(trackTest36)

trackTest37 = MaintenenceTracks("47", "Available")
trackList.append(trackTest37)

trackTest38 = MaintenenceTracks("48", "Available")
trackList.append(trackTest38)

trackTest39 = MaintenenceTracks("49", "Available")
trackList.append(trackTest39)

trackTest40 = MaintenenceTracks("50", "Available")
trackList.append(trackTest40)

trackTest41 = MaintenenceTracks("51", "Available")
trackList.append(trackTest41)

trackTest42 = MaintenenceTracks("52", "Available")
trackList.append(trackTest42)

trackTest43 = MaintenenceTracks("53", "Available")
trackList.append(trackTest43)

trackTest44 = MaintenenceTracks("54", "Available")
trackList.append(trackTest44)

trackTest45 = MaintenenceTracks("55", "Available")
trackList.append(trackTest45)

trackTest46 = MaintenenceTracks("56", "Available")
trackList.append(trackTest46)

trackTest47 = MaintenenceTracks("57", "Available")
trackList.append(trackTest47)

trackTest48 = MaintenenceTracks("58", "Available")
trackList.append(trackTest48)

trackTest49 = MaintenenceTracks("59", "Available")
trackList.append(trackTest49)

trackTest50 = MaintenenceTracks("60", "Available")
trackList.append(trackTest50)

gateTest = MaintenanceGates("9", "Available")
gateList.append(gateTest)

gateTest1 = MaintenanceGates("10", "Available")
gateList.append(gateTest1)

gateTest2 = MaintenanceGates("11", "Available")
gateList.append(gateTest2)

gateTest3 = MaintenanceGates("12", "Available")
gateList.append(gateTest3)

gateTest4 = MaintenanceGates("13", "Available")
gateList.append(gateTest4)

gateTest5 = MaintenanceGates("14", "Available")
gateList.append(gateTest5)

gateTest6 = MaintenanceGates("15", "Available")
gateList.append(gateTest6)

gateTest7 = MaintenanceGates("16", "Available")
gateList.append(gateTest7)

gateTest8 = MaintenanceGates("17", "Available")
gateList.append(gateTest8)

gateTest9 = MaintenanceGates("18", "Available")
gateList.append(gateTest9)

gateTest10 = MaintenanceGates("19", "Available")
gateList.append(gateTest10)

gateTest11 = MaintenanceGates("20", "Available")
gateList.append(gateTest11)

gateTest12 = MaintenanceGates("21", "Available")
gateList.append(gateTest12)

gateTest13 = MaintenanceGates("22", "Available")
gateList.append(gateTest13)

gateTest14 = MaintenanceGates("23", "Available")
gateList.append(gateTest14)

gateTest15 = MaintenanceGates("24", "Available")
gateList.append(gateTest15)

gateTest16 = MaintenanceGates("25", "Available")
gateList.append(gateTest16)

gateTest17 = MaintenanceGates("26", "Available")
gateList.append(gateTest17)

gateTest18 = MaintenanceGates("27", "Available")
gateList.append(gateTest18)

gateTest19 = MaintenanceGates("28", "Available")
gateList.append(gateTest19)

gateTest20 = MaintenanceGates("29", "Available")
gateList.append(gateTest20)

gateTest21 = MaintenanceGates("30", "Available")
gateList.append(gateTest21)

gateTest22 = MaintenanceGates("31", "Available")
gateList.append(gateTest22)

gateTest23 = MaintenanceGates("32", "Available")
gateList.append(gateTest23)

gateTest24 = MaintenanceGates("33", "Available")
gateList.append(gateTest24)

gateTest25 = MaintenanceGates("34", "Available")
gateList.append(gateTest25)

gateTest26 = MaintenanceGates("35", "Available")
gateList.append(gateTest26)

gateTest27 = MaintenanceGates("36", "Available")
gateList.append(gateTest27)

gateTest28 = MaintenanceGates("37", "Available")
gateList.append(gateTest28)

gateTest29 = MaintenanceGates("38", "Available")
gateList.append(gateTest29)

gateTest30 = MaintenanceGates("39", "Available")
gateList.append(gateTest30)

gateTest31 = MaintenanceGates("40", "Available")
gateList.append(gateTest31)

gateTest32 = MaintenanceGates("41", "Available")
gateList.append(gateTest32)

gateTest33 = MaintenanceGates("42", "Available")
gateList.append(gateTest33)

gateTest34 = MaintenanceGates("43", "Available")
gateList.append(gateTest34)

gateTest35 = MaintenanceGates("44", "Available")
gateList.append(gateTest35)

gateTest36 = MaintenanceGates("45", "Available")
gateList.append(gateTest36)

gateTest37 = MaintenanceGates("46", "Available")
gateList.append(gateTest37)

gateTest38 = MaintenanceGates("47", "Available")
gateList.append(gateTest38)

gateTest39 = MaintenanceGates("48", "Available")
gateList.append(gateTest39)

gateTest40 = MaintenanceGates("49", "Available")
gateList.append(gateTest40)

gateTest41 = MaintenanceGates("50", "Available")
gateList.append(gateTest41)

gateTest42 = MaintenanceGates("51", "Available")
gateList.append(gateTest42)

gateTest43 = MaintenanceGates("52", "Available")
gateList.append(gateTest43)

gateTest44 = MaintenanceGates("53", "Available")
gateList.append(gateTest44)

gateTest45 = MaintenanceGates("54", "Available")
gateList.append(gateTest45)

gateTest46 = MaintenanceGates("55", "Available")
gateList.append(gateTest46)

gateTest47 = MaintenanceGates("56", "Available")
gateList.append(gateTest47)

gateTest48 = MaintenanceGates("57", "Available")
gateList.append(gateTest48)

gateTest49 = MaintenanceGates("58", "Available")
gateList.append(gateTest49)

gateTest50 = MaintenanceGates("59", "Available")
gateList.append(gateTest50)

airlineTest = AirlineMaintenance("primera", 2019, "Local", 10)
airlineList.append(airlineTest)

airlineTest1 = AirlineMaintenance("segunda", 2019, "Local", 10)
airlineList.append(airlineTest1)

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

crewTest11 = CrewMaintenance("leo11", 18, 9, "primera", "Costumer service", "Available")
crewList.append(crewTest11)

crewTest12 = CrewMaintenance("leo12", 18, 21, "primera", "Pilot", "Available")
crewList.append(crewTest12)

crewTest13 = CrewMaintenance("leo13", 18, 10, "primera", "Costumer service", "Available")
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

crewTest19 = CrewMaintenance("leo19", 18, 27, "primera", "Pilot", "Available")
crewList.append(crewTest19)

crewTest20 = CrewMaintenance("leo20", 18, 28, "primera", "Pilot", "Available")
crewList.append(crewTest20)

crewTest21 = CrewMaintenance("leo21", 18, 29, "primera", "Pilot", "Available")
crewList.append(crewTest21)

crewTest22 = CrewMaintenance("leo22", 18, 30, "primera", "Costumer service", "Available")
crewList.append(crewTest22)

crewTest23 = CrewMaintenance("leo23", 18, 31, "primera", "Costumer service", "Available")
crewList.append(crewTest23)

crewTest24 = CrewMaintenance("leo24", 18, 32, "primera", "Costumer service", "Available")
crewList.append(crewTest24)

crewTest25 = CrewMaintenance("leo25", 18, 33, "primera", "Costumer service", "Available")
crewList.append(crewTest25)

crewTest26 = CrewMaintenance("leo26", 18, 34, "primera", "Costumer service", "Available")
crewList.append(crewTest26)

crewTest27 = CrewMaintenance("leo27", 18, 35, "primera", "Costumer service", "Available")
crewList.append(crewTest27)

crewTest28 = CrewMaintenance("leo28", 18, 36, "primera", "Costumer service", "Available")
crewList.append(crewTest28)

crewTest29 = CrewMaintenance("leo29", 18, 37, "primera", "Costumer service", "Available")
crewList.append(crewTest29)

crewTest30 = CrewMaintenance("leo30", 18, 38, "primera", "Pilot", "Available")
crewList.append(crewTest30)

crewTest31 = CrewMaintenance("leo31", 18, 39, "primera", "Costumer service", "Available")
crewList.append(crewTest31)

crewTest32 = CrewMaintenance("leo32", 18, 40, "primera", "Costumer service", "Available")
crewList.append(crewTest32)

crewTest33 = CrewMaintenance("leo33", 18, 41, "primera", "Costumer service", "Available")
crewList.append(crewTest33)

crewTest34 = CrewMaintenance("leo34", 18, 42, "primera", "Pilot", "Available")
crewList.append(crewTest34)

crewTest35 = CrewMaintenance("leo35", 18, 43, "primera", "Pilot", "Available")
crewList.append(crewTest35)

crewTest36 = CrewMaintenance("leo36", 18, 44, "primera", "Costumer service", "Available")
crewList.append(crewTest36)

crewTest37 = CrewMaintenance("leo37", 18, 45, "primera", "Pilot", "Available")
crewList.append(crewTest37)

crewTest38 = CrewMaintenance("leo38", 18, 46, "primera", "Pilot", "Available")
crewList.append(crewTest38)

crewTest39 = CrewMaintenance("leo39", 18, 47, "primera", "Pilot", "Available")
crewList.append(crewTest39)

crewTest40 = CrewMaintenance("leo40", 18, 48, "primera", "Costumer service", "Available")
crewList.append(crewTest40)

crewTest41 = CrewMaintenance("leo41", 18, 49, "primera", "Costumer service", "Available")
crewList.append(crewTest41)

crewTest42 = CrewMaintenance("leo42", 18, 50, "primera", "Costumer service", "Available")
crewList.append(crewTest42)

crewTest43 = CrewMaintenance("leo43", 18, 51, "primera", "Costumer service", "Available")
crewList.append(crewTest43)

crewTest44 = CrewMaintenance("leo44", 18, 52, "primera", "Costumer service", "Available")
crewList.append(crewTest44)

crewTest45 = CrewMaintenance("leo45", 18, 53, "primera", "Costumer service", "Available")
crewList.append(crewTest45)

crewTest46 = CrewMaintenance("leo46", 18, 54, "primera", "Costumer service", "Available")
crewList.append(crewTest46)

crewTest47 = CrewMaintenance("leo47", 18, 55, "primera", "Costumer service", "Available")
crewList.append(crewTest47)

crewTest48 = CrewMaintenance("leo48", 18, 56, "primera", "Pilot", "Available")
crewList.append(crewTest48)

crewTest49 = CrewMaintenance("leo49", 18, 57, "primera", "Costumer service", "Available")
crewList.append(crewTest49)

crewTest50 = CrewMaintenance("leo50", 18, 58, "primera", "Costumer service", "Available")
crewList.append(crewTest50)

crewTest51 = CrewMaintenance("leo51", 18, 59, "primera", "Costumer service", "Available")
crewList.append(crewTest51)

crewTest52 = CrewMaintenance("leo52", 18, 60, "primera", "Pilot", "Available")
crewList.append(crewTest52)

crewTest53 = CrewMaintenance("leo53", 18, 61, "primera", "Pilot", "Available")
crewList.append(crewTest53)

crewTest54 = CrewMaintenance("leo54", 18, 62, "primera", "Costumer service", "Available")
crewList.append(crewTest54)

crewTest55 = CrewMaintenance("leo55", 18, 63, "primera", "Pilot", "Available")
crewList.append(crewTest55)

crewTest56 = CrewMaintenance("leo56", 18, 64, "primera", "Pilot", "Available")
crewList.append(crewTest56)

crewTest57 = CrewMaintenance("leo57", 18, 65, "primera", "Pilot", "Available")
crewList.append(crewTest57)

crewTest58 = CrewMaintenance("leo58", 18, 66, "primera", "Costumer service", "Available")
crewList.append(crewTest58)

crewTest59 = CrewMaintenance("leo59", 18, 67, "primera", "Costumer service", "Available")
crewList.append(crewTest59)

crewTest60 = CrewMaintenance("leo60", 18, 68, "primera", "Costumer service", "Available")
crewList.append(crewTest60)

crewTest61 = CrewMaintenance("leo61", 18, 69, "primera", "Costumer service", "Available")
crewList.append(crewTest61)

crewTest62 = CrewMaintenance("leo62", 18, 70, "primera", "Costumer service", "Available")
crewList.append(crewTest62)

crewTest63 = CrewMaintenance("leo63", 18, 71, "primera", "Costumer service", "Available")
crewList.append(crewTest63)

crewTest64 = CrewMaintenance("leo64", 18, 72, "primera", "Costumer service", "Available")
crewList.append(crewTest64)

crewTest65 = CrewMaintenance("leo65", 18, 73, "primera", "Costumer service", "Available")
crewList.append(crewTest65)

crewTest66 = CrewMaintenance("leo66", 18, 74, "primera", "Pilot", "Available")
crewList.append(crewTest66)

crewTest67 = CrewMaintenance("leo67", 18, 75, "primera", "Costumer service", "Available")
crewList.append(crewTest67)

crewTest68 = CrewMaintenance("leo68", 18, 76, "primera", "Costumer service", "Available")
crewList.append(crewTest68)

crewTest69 = CrewMaintenance("leo69", 18, 77, "primera", "Costumer service", "Available")
crewList.append(crewTest69)

crewTest70 = CrewMaintenance("leo70", 18, 78, "primera", "Pilot", "Available")
crewList.append(crewTest70)

crewTest71 = CrewMaintenance("leo71", 18, 79, "primera", "Pilot", "Available")
crewList.append(crewTest71)

crewTest72 = CrewMaintenance("leo72", 18, 80, "primera", "Costumer service", "Available")
crewList.append(crewTest72)

crewTest73 = CrewMaintenance("leo73", 18, 81, "primera", "Pilot", "Available")
crewList.append(crewTest73)

crewTest74 = CrewMaintenance("leo74", 18, 82, "primera", "Pilot", "Available")
crewList.append(crewTest74)

crewTest75 = CrewMaintenance("leo75", 18, 83, "primera", "Pilot", "Available")
crewList.append(crewTest75)

crewTest76 = CrewMaintenance("leo76", 18, 84, "primera", "Costumer service", "Available")
crewList.append(crewTest76)

crewTest77 = CrewMaintenance("leo77", 18, 85, "primera", "Costumer service", "Available")
crewList.append(crewTest77)

crewTest78 = CrewMaintenance("leo78", 18, 86, "primera", "Costumer service", "Available")
crewList.append(crewTest78)

crewTest79 = CrewMaintenance("leo79", 18, 87, "primera", "Costumer service", "Available")
crewList.append(crewTest79)

crewTest80 = CrewMaintenance("leo80", 18, 88, "primera", "Costumer service", "Available")
crewList.append(crewTest80)

crewTest81 = CrewMaintenance("leo81", 18, 89, "primera", "Costumer service", "Available")
crewList.append(crewTest81)

crewTest82 = CrewMaintenance("leo82", 18, 90, "primera", "Costumer service", "Available")
crewList.append(crewTest82)

crewTest83 = CrewMaintenance("leo83", 18, 91, "primera", "Costumer service", "Available")
crewList.append(crewTest83)

crewTest84 = CrewMaintenance("leo84", 18, 92, "primera", "Pilot", "Available")
crewList.append(crewTest84)

crewTest85 = CrewMaintenance("leo85", 18, 93, "primera", "Costumer service", "Available")
crewList.append(crewTest85)

crewTest86 = CrewMaintenance("leo86", 18, 94, "primera", "Costumer service", "Available")
crewList.append(crewTest86)

crewTest87 = CrewMaintenance("leo87", 18, 95, "primera", "Costumer service", "Available")
crewList.append(crewTest87)

crewTest88 = CrewMaintenance("leo88", 18, 96, "primera", "Pilot", "Available")
crewList.append(crewTest88)

crewTest89 = CrewMaintenance("leo89", 18, 97, "primera", "Pilot", "Available")
crewList.append(crewTest89)

crewTest90 = CrewMaintenance("leo90", 18, 98, "primera", "Costumer service", "Available")
crewList.append(crewTest90)

crewTest91 = CrewMaintenance("leo91", 18, 99, "primera", "Pilot", "Available")
crewList.append(crewTest91)

crewTest92 = CrewMaintenance("leo92", 18, 100, "primera", "Pilot", "Available")
crewList.append(crewTest92)

crewTest93 = CrewMaintenance("leo93", 18, 101, "primera", "Pilot", "Available")
crewList.append(crewTest93)

crewTest94 = CrewMaintenance("leo94", 18, 102, "primera", "Costumer service", "Available")
crewList.append(crewTest94)

crewTest95 = CrewMaintenance("leo95", 18, 103, "primera", "Costumer service", "Available")
crewList.append(crewTest95)

crewTest96 = CrewMaintenance("leo96", 18, 104, "primera", "Costumer service", "Available")
crewList.append(crewTest96)

crewTest97 = CrewMaintenance("leo97", 18, 105, "primera", "Costumer service", "Available")
crewList.append(crewTest97)

crewTest98 = CrewMaintenance("leo98", 18, 106, "primera", "Costumer service", "Available")
crewList.append(crewTest98)

crewTest99 = CrewMaintenance("leo99", 18, 107, "primera", "Costumer service", "Available")
crewList.append(crewTest99)

crewTest100 = CrewMaintenance("leo100", 18, 108, "primera", "Costumer service", "Available")
crewList.append(crewTest100)

crewTest101 = CrewMaintenance("leo101", 18, 109, "primera", "Costumer service", "Available")
crewList.append(crewTest101)

crewTest102 = CrewMaintenance("leo102", 18, 110, "primera", "Pilot", "Available")
crewList.append(crewTest102)

crewTest103 = CrewMaintenance("leo103", 18, 111, "primera", "Costumer service", "Available")
crewList.append(crewTest103)

crewTest104 = CrewMaintenance("leo104", 18, 112, "primera", "Costumer service", "Available")
crewList.append(crewTest104)

crewTest105 = CrewMaintenance("leo105", 18, 113, "primera", "Costumer service", "Available")
crewList.append(crewTest105)

crewTest106 = CrewMaintenance("leo106", 18, 114, "primera", "Pilot", "Available")
crewList.append(crewTest106)

crewTest107 = CrewMaintenance("leo107", 18, 115, "primera", "Pilot", "Available")
crewList.append(crewTest107)

crewTest108 = CrewMaintenance("leo108", 18, 116, "primera", "Costumer service", "Available")
crewList.append(crewTest108)

crewTest109 = CrewMaintenance("leo109", 18, 118, "primera", "Pilot", "Available")
crewList.append(crewTest109)

crewTest110 = CrewMaintenance("leo110", 18, 119, "primera", "Pilot", "Available")
crewList.append(crewTest110)

crewTest111 = CrewMaintenance("leo111", 18, 120, "primera", "Costumer service", "Available")
crewList.append(crewTest111)

crewTest112 = CrewMaintenance("leo112", 18, 121, "primera", "Costumer service", "Available")
crewList.append(crewTest112)

crewTest113 = CrewMaintenance("leo113", 18, 122, "primera", "Costumer service", "Available")
crewList.append(crewTest113)

crewTest114 = CrewMaintenance("leo114", 18, 123, "primera", "Costumer service", "Available")
crewList.append(crewTest114)

crewTest115 = CrewMaintenance("leo115", 18, 124, "primera", "Costumer service", "Available")
crewList.append(crewTest115)

crewTest116 = CrewMaintenance("leo116", 18, 125, "primera", "Costumer service", "Available")
crewList.append(crewTest116)

crewTest117 = CrewMaintenance("leo117", 18, 126, "primera", "Costumer service", "Available")
crewList.append(crewTest117)

crewTest118 = CrewMaintenance("leo118", 18, 127, "primera", "Costumer service", "Available")
crewList.append(crewTest118)

crewTest119 = CrewMaintenance("leo119", 18, 128, "primera", "Pilot", "Available")
crewList.append(crewTest119)

crewTest120 = CrewMaintenance("leo120", 18, 129, "primera", "Costumer service", "Available")
crewList.append(crewTest120)

crewTest121 = CrewMaintenance("leo121", 18, 130, "primera", "Costumer service", "Available")
crewList.append(crewTest121)

crewTest122 = CrewMaintenance("leo122", 18, 131, "primera", "Costumer service", "Available")
crewList.append(crewTest122)

crewTest123 = CrewMaintenance("leo123", 18, 132, "primera", "Pilot", "Available")
crewList.append(crewTest123)

crewTest124 = CrewMaintenance("leo124", 18, 133, "primera", "Pilot", "Available")
crewList.append(crewTest124)

crewTest125 = CrewMaintenance("leo125", 18, 134, "primera", "Costumer service", "Available")
crewList.append(crewTest125)

crewTest251 = CrewMaintenance("leo251", 18, 251, "primera", "Pilot", "Available")
crewList.append(crewTest251)

crewTest252 = CrewMaintenance("leo252", 18, 252, "primera", "Pilot", "Available")
crewList.append(crewTest252)

crewTest253 = CrewMaintenance("leo253", 18, 253, "primera", "Pilot", "Available")
crewList.append(crewTest253)

crewTest254 = CrewMaintenance("leo254", 18, 254, "primera", "Pilot", "Available")
crewList.append(crewTest254)

crewTest255 = CrewMaintenance("leo255", 18, 255, "primera", "Pilot", "Available")
crewList.append(crewTest255)

crewTest256 = CrewMaintenance("leo256", 18, 256, "primera", "Pilot", "Available")
crewList.append(crewTest256)

crewTest257 = CrewMaintenance("leo257", 18, 257, "primera", "Pilot", "Available")
crewList.append(crewTest257)

crewTest258 = CrewMaintenance("leo258", 18, 258, "primera", "Pilot", "Available")
crewList.append(crewTest258)

crewTest259 = CrewMaintenance("leo259", 18, 259, "primera", "Pilot", "Available")
crewList.append(crewTest259)

crewTest260 = CrewMaintenance("leo260", 18, 260, "primera", "Pilot", "Available")
crewList.append(crewTest260)

crewTest261 = CrewMaintenance("leo261", 18, 261, "primera", "Pilot", "Available")
crewList.append(crewTest261)

crewTest262 = CrewMaintenance("leo262", 18, 262, "primera", "Pilot", "Available")
crewList.append(crewTest262)

crewTest126 = CrewMaintenance("leo126", 18, 135, "segunda", "Pilot", "Available")
crewList.append(crewTest126)

crewTest127 = CrewMaintenance("leo127", 18, 136, "segunda", "Pilot", "Available")
crewList.append(crewTest127)

crewTest128 = CrewMaintenance("leo128", 18, 137, "segunda", "Pilot", "Available")
crewList.append(crewTest128)

crewTest129 = CrewMaintenance("leo129", 18, 138, "segunda", "Costumer service", "Available")
crewList.append(crewTest129)

crewTest130 = CrewMaintenance("leo130", 18, 139, "segunda", "Costumer service", "Available")
crewList.append(crewTest130)

crewTest131 = CrewMaintenance("leo131", 18, 140, "segunda", "Costumer service", "Available")
crewList.append(crewTest131)

crewTest132 = CrewMaintenance("leo132", 18, 141, "segunda", "Costumer service", "Available")
crewList.append(crewTest132)

crewTest133 = CrewMaintenance("leo133", 18, 142, "segunda", "Costumer service", "Available")
crewList.append(crewTest133)

crewTest134 = CrewMaintenance("leo134", 18, 143, "segunda", "Costumer service", "Available")
crewList.append(crewTest134)

crewTest135 = CrewMaintenance("leo135", 18, 144, "segunda", "Costumer service", "Available")
crewList.append(crewTest135)

crewTest136 = CrewMaintenance("leo136", 18, 145, "segunda", "Costumer service", "Available")
crewList.append(crewTest136)

crewTest137 = CrewMaintenance("leo137", 18, 146, "segunda", "Pilot", "Available")
crewList.append(crewTest137)

crewTest138 = CrewMaintenance("leo138", 18, 147, "segunda", "Costumer service", "Available")
crewList.append(crewTest138)

crewTest139 = CrewMaintenance("leo139", 18, 148, "segunda", "Costumer service", "Available")
crewList.append(crewTest139)

crewTest140 = CrewMaintenance("leo140", 18, 149, "segunda", "Costumer service", "Available")
crewList.append(crewTest140)

crewTest141 = CrewMaintenance("leo141", 18, 150, "segunda", "Pilot", "Available")
crewList.append(crewTest141)

crewTest142 = CrewMaintenance("leo142", 18, 151, "segunda", "Pilot", "Available")
crewList.append(crewTest142)

crewTest143 = CrewMaintenance("leo143", 18, 152, "segunda", "Costumer service", "Available")
crewList.append(crewTest143)

crewTest144 = CrewMaintenance("leo144", 18, 153, "segunda", "Pilot", "Available")
crewList.append(crewTest144)

crewTest145 = CrewMaintenance("leo145", 18, 154, "segunda", "Pilot", "Available")
crewList.append(crewTest145)

crewTest146 = CrewMaintenance("leo146", 18, 155, "segunda", "Pilot", "Available")
crewList.append(crewTest146)

crewTest147 = CrewMaintenance("leo147", 18, 156, "segunda", "Costumer service", "Available")
crewList.append(crewTest147)

crewTest148 = CrewMaintenance("leo148", 18, 157, "segunda", "Costumer service", "Available")
crewList.append(crewTest148)

crewTest149 = CrewMaintenance("leo149", 18, 158, "segunda", "Costumer service", "Available")
crewList.append(crewTest148)

crewTest150 = CrewMaintenance("leo150", 18, 159, "segunda", "Costumer service", "Available")
crewList.append(crewTest150)

crewTest151 = CrewMaintenance("leo151", 18, 160, "segunda", "Costumer service", "Available")
crewList.append(crewTest151)

crewTest152 = CrewMaintenance("leo152", 18, 161, "segunda", "Costumer service", "Available")
crewList.append(crewTest152)

crewTest153 = CrewMaintenance("leo153", 18, 162, "segunda", "Costumer service", "Available")
crewList.append(crewTest153)

crewTest154 = CrewMaintenance("leo154", 18, 163, "segunda", "Costumer service", "Available")
crewList.append(crewTest154)

crewTest155 = CrewMaintenance("leo155", 18, 164, "segunda", "Pilot", "Available")
crewList.append(crewTest155)

crewTest156 = CrewMaintenance("leo156", 18, 165, "segunda", "Costumer service", "Available")
crewList.append(crewTest156)

crewTest157 = CrewMaintenance("leo157", 18, 166, "segunda", "Costumer service", "Available")
crewList.append(crewTest157)

crewTest158 = CrewMaintenance("leo158", 18, 167, "segunda", "Costumer service", "Available")
crewList.append(crewTest158)

crewTest159 = CrewMaintenance("leo159", 18, 168, "segunda", "Pilot", "Available")
crewList.append(crewTest159)

crewTest160 = CrewMaintenance("leo160", 18, 169, "segunda", "Pilot", "Available")
crewList.append(crewTest160)

crewTest161 = CrewMaintenance("leo161", 18, 170, "segunda", "Costumer service", "Available")
crewList.append(crewTest161)

crewTest162 = CrewMaintenance("leo162", 18, 171, "segunda", "Pilot", "Available")
crewList.append(crewTest162)

crewTest163 = CrewMaintenance("leo163", 18, 172, "segunda", "Pilot", "Available")
crewList.append(crewTest163)

crewTest164 = CrewMaintenance("leo164", 18, 173, "segunda", "Pilot", "Available")
crewList.append(crewTest164)

crewTest165 = CrewMaintenance("leo165", 18, 174, "segunda", "Costumer service", "Available")
crewList.append(crewTest165)

crewTest166 = CrewMaintenance("leo166", 18, 175, "segunda", "Costumer service", "Available")
crewList.append(crewTest166)

crewTest167 = CrewMaintenance("leo167", 18, 176, "segunda", "Costumer service", "Available")
crewList.append(crewTest167)

crewTest168 = CrewMaintenance("leo168", 18, 177, "segunda", "Costumer service", "Available")
crewList.append(crewTest168)

crewTest169 = CrewMaintenance("leo169", 18, 178, "segunda", "Costumer service", "Available")
crewList.append(crewTest169)

crewTest170 = CrewMaintenance("leo170", 18, 179, "segunda", "Costumer service", "Available")
crewList.append(crewTest170)

crewTest171 = CrewMaintenance("leo171", 18, 180, "segunda", "Costumer service", "Available")
crewList.append(crewTest171)

crewTest172 = CrewMaintenance("leo172", 18, 181, "segunda", "Costumer service", "Available")
crewList.append(crewTest172)

crewTest173 = CrewMaintenance("leo173", 18, 182, "segunda", "Pilot", "Available")
crewList.append(crewTest173)

crewTest174 = CrewMaintenance("leo174", 18, 183, "segunda", "Costumer service", "Available")
crewList.append(crewTest174)

crewTest175 = CrewMaintenance("leo175", 18, 184, "segunda", "Costumer service", "Available")
crewList.append(crewTest175)

crewTest176 = CrewMaintenance("leo176", 18, 185, "segunda", "Costumer service", "Available")
crewList.append(crewTest176)

crewTest177 = CrewMaintenance("leo177", 18, 186, "segunda", "Pilot", "Available")
crewList.append(crewTest177)

crewTest178 = CrewMaintenance("leo178", 18, 187, "segunda", "Pilot", "Available")
crewList.append(crewTest178)

crewTest179 = CrewMaintenance("leo179", 18, 188, "segunda", "Costumer service", "Available")
crewList.append(crewTest179)

crewTest180 = CrewMaintenance("leo180", 18, 189, "segunda", "Pilot", "Available")
crewList.append(crewTest180)

crewTest181 = CrewMaintenance("leo181", 18, 190, "segunda", "Pilot", "Available")
crewList.append(crewTest181)

crewTest182 = CrewMaintenance("leo182", 18, 191, "segunda", "Pilot", "Available")
crewList.append(crewTest182)

crewTest183 = CrewMaintenance("leo183", 18, 192, "segunda", "Costumer service", "Available")
crewList.append(crewTest183)

crewTest184 = CrewMaintenance("leo184", 18, 193, "segunda", "Costumer service", "Available")
crewList.append(crewTest184)

crewTest185 = CrewMaintenance("leo185", 18, 194, "segunda", "Costumer service", "Available")
crewList.append(crewTest185)

crewTest186 = CrewMaintenance("leo186", 18, 195, "segunda", "Costumer service", "Available")
crewList.append(crewTest186)

crewTest187 = CrewMaintenance("leo187", 18, 196, "segunda", "Costumer service", "Available")
crewList.append(crewTest187)

crewTest188 = CrewMaintenance("leo188", 18, 197, "segunda", "Costumer service", "Available")
crewList.append(crewTest188)

crewTest189 = CrewMaintenance("leo189", 18, 198, "segunda", "Costumer service", "Available")
crewList.append(crewTest189)

crewTest190 = CrewMaintenance("leo190", 18, 199, "segunda", "Costumer service", "Available")
crewList.append(crewTest190)

crewTest191 = CrewMaintenance("leo191", 18, 200, "segunda", "Pilot", "Available")
crewList.append(crewTest191)

crewTest192 = CrewMaintenance("leo192", 18, 201, "segunda", "Costumer service", "Available")
crewList.append(crewTest192)

crewTest193 = CrewMaintenance("leo193", 18, 202, "segunda", "Costumer service", "Available")
crewList.append(crewTest193)

crewTest194 = CrewMaintenance("leo194", 18, 203, "segunda", "Costumer service", "Available")
crewList.append(crewTest194)

crewTest195 = CrewMaintenance("leo195", 18, 204, "segunda", "Pilot", "Available")
crewList.append(crewTest195)

crewTest196 = CrewMaintenance("leo196", 18, 205, "segunda", "Pilot", "Available")
crewList.append(crewTest196)

crewTest197 = CrewMaintenance("leo197", 18, 206, "segunda", "Costumer service", "Available")
crewList.append(crewTest197)

crewTest198 = CrewMaintenance("leo198", 18, 207, "segunda", "Pilot", "Available")
crewList.append(crewTest198)

crewTest199 = CrewMaintenance("leo199", 18, 208, "segunda", "Pilot", "Available")
crewList.append(crewTest199)

crewTest200 = CrewMaintenance("leo200", 18, 209, "segunda", "Pilot", "Available")
crewList.append(crewTest200)

crewTest201 = CrewMaintenance("leo201", 18, 210, "segunda", "Costumer service", "Available")
crewList.append(crewTest201)

crewTest202 = CrewMaintenance("leo202", 18, 211, "segunda", "Costumer service", "Available")
crewList.append(crewTest202)

crewTest203 = CrewMaintenance("leo203", 18, 212, "segunda", "Costumer service", "Available")
crewList.append(crewTest203)

crewTest204 = CrewMaintenance("leo204", 18, 213, "segunda", "Costumer service", "Available")
crewList.append(crewTest204)

crewTest205 = CrewMaintenance("leo205", 18, 214, "segunda", "Costumer service", "Available")
crewList.append(crewTest205)

crewTest206 = CrewMaintenance("leo206", 18, 215, "segunda", "Costumer service", "Available")
crewList.append(crewTest206)

crewTest207 = CrewMaintenance("leo207", 18, 216, "segunda", "Costumer service", "Available")
crewList.append(crewTest207)

crewTest208 = CrewMaintenance("leo208", 18, 217, "segunda", "Costumer service", "Available")
crewList.append(crewTest208)

crewTest209 = CrewMaintenance("leo209", 18, 218, "segunda", "Pilot", "Available")
crewList.append(crewTest209)

crewTest210 = CrewMaintenance("leo210", 18, 219, "segunda", "Costumer service", "Available")
crewList.append(crewTest210)

crewTest211 = CrewMaintenance("leo211", 18, 220, "segunda", "Costumer service", "Available")
crewList.append(crewTest211)

crewTest212 = CrewMaintenance("leo212", 18, 221, "segunda", "Costumer service", "Available")
crewList.append(crewTest212)

crewTest213 = CrewMaintenance("leo213", 18, 222, "segunda", "Pilot", "Available")
crewList.append(crewTest213)

crewTest214 = CrewMaintenance("leo214", 18, 223, "segunda", "Pilot", "Available")
crewList.append(crewTest214)

crewTest215 = CrewMaintenance("leo215", 18, 224, "segunda", "Costumer service", "Available")
crewList.append(crewTest215)

crewTest216 = CrewMaintenance("leo216", 18, 225, "segunda", "Pilot", "Available")
crewList.append(crewTest216)

crewTest217 = CrewMaintenance("leo217", 18, 226, "segunda", "Pilot", "Available")
crewList.append(crewTest217)

crewTest218 = CrewMaintenance("leo218", 18, 227, "segunda", "Pilot", "Available")
crewList.append(crewTest218)

crewTest219 = CrewMaintenance("leo219", 18, 228, "segunda", "Costumer service", "Available")
crewList.append(crewTest219)

crewTest220 = CrewMaintenance("leo220", 18, 229, "segunda", "Costumer service", "Available")
crewList.append(crewTest220)

crewTest221 = CrewMaintenance("leo221", 18, 230, "segunda", "Costumer service", "Available")
crewList.append(crewTest221)

crewTest222 = CrewMaintenance("leo222", 18, 231, "segunda", "Costumer service", "Available")
crewList.append(crewTest222)

crewTest223 = CrewMaintenance("leo223", 18, 232, "segunda", "Costumer service", "Available")
crewList.append(crewTest223)

crewTest224 = CrewMaintenance("leo224", 18, 233, "segunda", "Costumer service", "Available")
crewList.append(crewTest224)

crewTest225 = CrewMaintenance("leo225", 18, 234, "segunda", "Costumer service", "Available")
crewList.append(crewTest225)

crewTest226 = CrewMaintenance("leo226", 18, 235, "segunda", "Costumer service", "Available")
crewList.append(crewTest226)

crewTest227 = CrewMaintenance("leo227", 18, 236, "segunda", "Pilot", "Available")
crewList.append(crewTest227)

crewTest228 = CrewMaintenance("leo228", 18, 237, "segunda", "Costumer service", "Available")
crewList.append(crewTest228)

crewTest229 = CrewMaintenance("leo229", 18, 238, "segunda", "Costumer service", "Available")
crewList.append(crewTest229)

crewTest230 = CrewMaintenance("leo230", 18, 239, "segunda", "Costumer service", "Available")
crewList.append(crewTest230)

crewTest231 = CrewMaintenance("leo231", 18, 240, "segunda", "Pilot", "Available")
crewList.append(crewTest231)

crewTest232 = CrewMaintenance("leo232", 18, 241, "segunda", "Pilot", "Available")
crewList.append(crewTest232)

crewTest233 = CrewMaintenance("leo233", 18, 242, "segunda", "Costumer service", "Available")
crewList.append(crewTest233)

crewTest234 = CrewMaintenance("leo234", 18, 243, "segunda", "Pilot", "Available")
crewList.append(crewTest234)

crewTest235 = CrewMaintenance("leo235", 18, 244, "segunda", "Pilot", "Available")
crewList.append(crewTest235)

crewTest236 = CrewMaintenance("leo236", 18, 245, "segunda", "Pilot", "Available")
crewList.append(crewTest236)

crewTest237 = CrewMaintenance("leo237", 18, 245, "segunda", "Costumer service", "Available")
crewList.append(crewTest237)

crewTest238 = CrewMaintenance("leo238", 18, 246, "segunda", "Costumer service", "Available")
crewList.append(crewTest238)

crewTest239 = CrewMaintenance("leo239", 18, 247, "segunda", "Costumer service", "Available")
crewList.append(crewTest239)

crewTest240 = CrewMaintenance("leo240", 18, 248, "segunda", "Costumer service", "Available")
crewList.append(crewTest240)

crewTest241 = CrewMaintenance("leo241", 18, 249, "segunda", "Costumer service", "Available")
crewList.append(crewTest241)

crewTest242 = CrewMaintenance("leo242", 18, 250, "segunda", "Costumer service", "Available")
crewList.append(crewTest242)

crewTest243 = CrewMaintenance("leo243", 18, 251, "segunda", "Costumer service", "Available")
crewList.append(crewTest243)

crewTest244 = CrewMaintenance("leo244", 18, 252, "segunda", "Costumer service", "Available")
crewList.append(crewTest244)

crewTest245 = CrewMaintenance("leo245", 18, 253, "segunda", "Pilot", "Available")
crewList.append(crewTest245)

crewTest246 = CrewMaintenance("leo246", 18, 254, "segunda", "Costumer service", "Available")
crewList.append(crewTest246)

crewTest247 = CrewMaintenance("leo247", 18, 255, "segunda", "Costumer service", "Available")
crewList.append(crewTest247)

crewTest248 = CrewMaintenance("leo248", 18, 256, "segunda", "Costumer service", "Available")
crewList.append(crewTest248)

crewTest249 = CrewMaintenance("leo249", 18, 257, "segunda", "Pilot", "Available")
crewList.append(crewTest249)

crewTest250 = CrewMaintenance("leo250", 18, 258, "segunda", "Pilot", "Available")
crewList.append(crewTest250)

crewTest249 = CrewMaintenance("leo249", 18, 257, "segunda", "Pilot", "Available")
crewList.append(crewTest249)

crewTest250 = CrewMaintenance("leo250", 18, 258, "segunda", "Pilot", "Available")
crewList.append(crewTest250)

crewTest270 = CrewMaintenance("leo270", 18, 270, "segunda", "Pilot", "Available")
crewList.append(crewTest270)

crewTest271 = CrewMaintenance("leo271", 18, 271, "segunda", "Pilot", "Available")
crewList.append(crewTest271)

crewTest272 = CrewMaintenance("leo272", 18, 272, "segunda", "Pilot", "Available")
crewList.append(crewTest272)

crewTest273 = CrewMaintenance("leo273", 18, 273, "segunda", "Pilot", "Available")
crewList.append(crewTest273)

crewTest274 = CrewMaintenance("leo274", 18, 274, "segunda", "Pilot", "Available")
crewList.append(crewTest274)

crewTest275 = CrewMaintenance("leo275", 18, 275, "segunda", "Pilot", "Available")
crewList.append(crewTest275)

crewTest276 = CrewMaintenance("leo276", 18, 276, "segunda", "Pilot", "Available")
crewList.append(crewTest276)

crewTest277 = CrewMaintenance("leo277", 18, 277, "segunda", "Pilot", "Available")
crewList.append(crewTest277)

crewTest278 = CrewMaintenance("leo278", 18, 278, "segunda", "Pilot", "Available")
crewList.append(crewTest278)

crewTest279 = CrewMaintenance("leo279", 18, 279, "segunda", "Pilot", "Available")
crewList.append(crewTest279)

crewTest280 = CrewMaintenance("leo280", 18, 280, "segunda", "Pilot", "Available")
crewList.append(crewTest280)

crewTest281 = CrewMaintenance("leo281", 18, 281, "segunda", "Pilot", "Available")
crewList.append(crewTest281)

crewTest282 = CrewMaintenance("leo282", 18, 282, "segunda", "Pilot", "Available")
crewList.append(crewTest282)

crewTest283 = CrewMaintenance("leo283", 18, 283, "segunda", "Pilot", "Available")
crewList.append(crewTest283)

airportTest1 = AirportMaintenance("Tacos Airport", "Cancun", "Mexico")
airportList.append(airportTest1)

airportTest2 = AirportMaintenance("Texas Airport", "Texas", "USA")
airportList.append(airportTest2)

airportTest3 = AirportMaintenance("Juan SantaMaria Airport", "Alajuela", "Costa Rica")
airportList.append(airportTest3)

airportTest4 = AirportMaintenance("Bogota Airport", "Bogota", "Colombia")
airportList.append(airportTest4)

airportTest5 = AirportMaintenance("Brasilia Airport", "Brasilia", "Brasil")
airportList.append(airportTest5)

airportTest6 = AirportMaintenance("Barcelona Airport", "Cataluna", "Espana")
airportList.append(airportTest6)

airportTest7 = AirportMaintenance("Managua Airport", "Managua", "Nicaragua")
airportList.append(airportTest7)

airportTest8 = AirportMaintenance("Buenos Aires Airport", "Buenos Aires", "Argentina")
airportList.append(airportTest8)

airportTest9 = AirportMaintenance("Canada Airport", "Toronto", "Canada")
airportList.append(airportTest9)

airportTest10 = AirportMaintenance("Honduras Airport", "Tegucigalpa", "Hounduras")
airportList.append(airportTest10)

airportTest11 = AirportMaintenance("Russia Airport", "Moscow", "Russia")
airportList.append(airportTest11)

airportTest12 = AirportMaintenance("Chile Airport", "Santiago", "Chile")
airportList.append(airportTest12)

airportTest13 = AirportMaintenance("Peru Airport", "Cuzco", "Peru")
airportList.append(airportTest13)

airportTest14 = AirportMaintenance("Italy Airport", "Rome", "Italy")
airportList.append(airportTest14)

airportTest15 = AirportMaintenance("Panama Airport", "Panama City", "Panama")
airportList.append(airportTest15)

airportTest16 = AirportMaintenance("Guatemala Airport", "Guatemala City", "Guatemala")
airportList.append(airportTest16)

airportTest17 = AirportMaintenance("Uruguay Airport", "Montevideo", "Guatemala")
airportList.append(airportTest17)

airportTest18 = AirportMaintenance("Paraguay Airport", "Asuncion", "Paraguay")
airportList.append(airportTest18)

airportTest19 = AirportMaintenance("Bolivia Airport", "Sucre", "Bolivia")
airportList.append(airportTest19)

airportTest20 = AirportMaintenance("Venezuela Airport", "Caracas", "Venezuela")
airportList.append(airportTest20)

airportTest21 = AirportMaintenance("Ecuador Airport", "Quito", "Ecuador")
airportList.append(airportTest21)

airportTest22 = AirportMaintenance("Jamaica Airport", "Kingston", "Jamaica")
airportList.append(airportTest22)

airportTest23 = AirportMaintenance("Cuba Airport", "Habana", "Cuba")
airportList.append(airportTest23)

airportTest24 = AirportMaintenance("Haiti Airport", "Puerto Principe", "Haiti")
airportList.append(airportTest24)

aircraftTest = PlaneMaintenance("1", 2019, "1", "primera", 100, "Available")
aircraftList.append(aircraftTest)

aircraftTest1 = PlaneMaintenance("2", 2019, "2", "primera", 100, "Available")
aircraftList.append(aircraftTest1)

aircraftTest2 = PlaneMaintenance("3", 2019, "3", "primera", 100, "Available")
aircraftList.append(aircraftTest2)

aircraftTest3 = PlaneMaintenance("4", 2019, "4", "primera", 100, "Available")
aircraftList.append(aircraftTest3)

aircraftTest4 = PlaneMaintenance("5", 2019, "5", "primera", 100, "Available")
aircraftList.append(aircraftTest4)

aircraftTest5 = PlaneMaintenance("6", 2019, "6", "primera", 100, "Available")
aircraftList.append(aircraftTest5)

aircraftTest6 = PlaneMaintenance("7", 2019, "7", "primera", 100, "Available")
aircraftList.append(aircraftTest6)

aircraftTest7 = PlaneMaintenance("8", 2019, "8", "primera", 100, "Available")
aircraftList.append(aircraftTest7)

aircraftTest8 = PlaneMaintenance("9", 2019, "9", "primera", 100, "Available")
aircraftList.append(aircraftTest8)

aircraftTest9 = PlaneMaintenance("10", 2019, "10", "primera", 100, "Available")
aircraftList.append(aircraftTest9)

aircraftTest10 = PlaneMaintenance("11", 2019, "11", "primera", 100, "Available")
aircraftList.append(aircraftTest10)

aircraftTest11 = PlaneMaintenance("12", 2019, "12", "primera", 100, "Available")
aircraftList.append(aircraftTest11)

aircraftTest12 = PlaneMaintenance("13", 2019, "13", "primera", 100, "Available")
aircraftList.append(aircraftTest12)

aircraftTest13 = PlaneMaintenance("14", 2019, "14", "primera", 100, "Available")
aircraftList.append(aircraftTest13)

aircraftTest14 = PlaneMaintenance("15", 2019, "15", "primera", 100, "Available")
aircraftList.append(aircraftTest14)

aircraftTest15 = PlaneMaintenance("16", 2019, "16", "primera", 100, "Available")
aircraftList.append(aircraftTest15)

aircraftTest16 = PlaneMaintenance("17", 2019, "17", "primera", 100, "Available")
aircraftList.append(aircraftTest16)

aircraftTest17 = PlaneMaintenance("18", 2019, "18", "primera", 100, "Available")
aircraftList.append(aircraftTest17)

aircraftTest18 = PlaneMaintenance("19", 2019, "19", "primera", 100, "Available")
aircraftList.append(aircraftTest18)

aircraftTest19 = PlaneMaintenance("20", 2019, "20", "primera", 100, "Available")
aircraftList.append(aircraftTest19)

aircraftTest20 = PlaneMaintenance("21", 2019, "21", "primera", 100, "Available")
aircraftList.append(aircraftTest20)

aircraftTest21 = PlaneMaintenance("22", 2019, "22", "primera", 10, "Available")
aircraftList.append(aircraftTest21)

aircraftTest22 = PlaneMaintenance("23", 2019, "23", "primera", 100, "Available")
aircraftList.append(aircraftTest22)

aircraftTest23 = PlaneMaintenance("24", 2019, "24", "primera", 100, "Available")
aircraftList.append(aircraftTest23)

aircraftTest24 = PlaneMaintenance("25", 2019, "25", "primera", 100, "Available")
aircraftList.append(aircraftTest24)

aircraftTest25 = PlaneMaintenance("26", 2019, "26", "primera", 100, "Available")
aircraftList.append(aircraftTest25)

aircraftTest26 = PlaneMaintenance("27", 2019, "27", "segunda", 100, "Available")
aircraftList.append(aircraftTest26)

aircraftTest27 = PlaneMaintenance("28", 2019, "28", "segunda", 100, "Available")
aircraftList.append(aircraftTest27)

aircraftTest28 = PlaneMaintenance("29", 2019, "29", "segunda", 100, "Available")
aircraftList.append(aircraftTest28)

aircraftTest29 = PlaneMaintenance("30", 2019, "30", "segunda", 100, "Available")
aircraftList.append(aircraftTest29)

aircraftTest30 = PlaneMaintenance("31", 2019, "31", "segunda", 100, "Available")
aircraftList.append(aircraftTest30)

aircraftTest31 = PlaneMaintenance("32", 2019, "32", "segunda", 100, "Available")
aircraftList.append(aircraftTest31)

aircraftTest32 = PlaneMaintenance("33", 2019, "33", "segunda", 100, "Available")
aircraftList.append(aircraftTest32)

aircraftTest33 = PlaneMaintenance("34", 2019, "34", "segunda", 100, "Available")
aircraftList.append(aircraftTest33)

aircraftTest34 = PlaneMaintenance("35", 2019, "35", "segunda", 100, "Available")
aircraftList.append(aircraftTest34)

aircraftTest35 = PlaneMaintenance("36", 2019, "36", "segunda", 100, "Available")
aircraftList.append(aircraftTest35)

aircraftTest36 = PlaneMaintenance("37", 2019, "37", "segunda", 100, "Available")
aircraftList.append(aircraftTest36)

aircraftTest37 = PlaneMaintenance("38", 2019, "38", "segunda", 100, "Available")
aircraftList.append(aircraftTest37)

aircraftTest38 = PlaneMaintenance("39", 2019, "39", "segunda", 100, "Available")
aircraftList.append(aircraftTest38)

aircraftTest39 = PlaneMaintenance("40", 2019, "40", "segunda", 100, "Available")
aircraftList.append(aircraftTest39)

aircraftTest40 = PlaneMaintenance("41", 2019, "41", "segunda", 100, "Available")
aircraftList.append(aircraftTest40)

aircraftTest41 = PlaneMaintenance("42", 2019, "42", "segunda", 100, "Available")
aircraftList.append(aircraftTest41)

aircraftTest42 = PlaneMaintenance("43", 2019, "43", "segunda", 100, "Available")
aircraftList.append(aircraftTest42)

aircraftTest43 = PlaneMaintenance("44", 2019, "44", "segunda", 100, "Available")
aircraftList.append(aircraftTest43)

aircraftTest44 = PlaneMaintenance("45", 2019, "45", "segunda", 100, "Available")
aircraftList.append(aircraftTest44)

aircraftTest45 = PlaneMaintenance("46", 2019, "46", "segunda", 100, "Available")
aircraftList.append(aircraftTest45)

aircraftTest46 = PlaneMaintenance("47", 2019, "47", "segunda", 100, "Available")
aircraftList.append(aircraftTest46)

aircraftTest47 = PlaneMaintenance("48", 2019, "48", "segunda", 100, "Available")
aircraftList.append(aircraftTest47)

aircraftTest48 = PlaneMaintenance("49", 2019, "49", "segunda", 100, "Available")
aircraftList.append(aircraftTest48)

aircraftTest49 = PlaneMaintenance("50", 2019, "50", "segunda", 100, "Available")
aircraftList.append(aircraftTest49)

'------------------------------------------#Rules or Variables---------------------------------------'
"""strDate = '2/4/18'
objDate = datetime.strptime(strDate, '%m/%d/%y')
objDate
datetime.datetime(2018, 2, 4, 0, 0)
datetime.strftime(objDate,'%b %d, %Y')
'Feb 04, 2018'
datetime.strftime(objDate,'%Y')"""

'------------------------------------------#Fuctions---------------------------------------'


# Procedure to add Users in the User object
def addUser(name, age, email, id, password, role):
    newUser = User(name, age, email, id, password, role)
    usersList.append(newUser)


# Procedure to show the info of user
def showInfoUser():
    if usersList != []:
        for user in usersList:
            print("Name: ", user.name, "Age: ", user.age,
                  "Email: ", user.email, "ID: ", user.id,
                  "Password:", user.password, "Role:", user.role)
    else:
        print("\nNo users found\n")


# Procedure to verify the id is not repeated
def verifyID(id):
    for user in usersList:
        if id == user.id:
            return True
    else:
        return False


# Procedure to verify the Email is not repeated
def verifyEmail(email):
    for user in usersList:
        if email == user.email:
            return True
    else:
        return False


# Procedure to validate the login
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


# Procedure to add a track in the Track object
def addTrack(number, status):
    newTrack = MaintenenceTracks(number, status)
    trackList.append(newTrack)


# Procedure to verify the track is not repeated
def verifyTrack(number):
    for track in trackList:
        if number == track.number:
            return True
    else:
        return False


# Procedure to show the tracks
def showTracks():
    if trackList != []:
        for track in trackList:
            print("Track Number: ", track.number, "Status: ", track.status)
    else:
        print("\nNo tracks found\n")


# Procedure to modify the track
def modifyTrack(number, status):
    for track in trackList:
        if track.number == number:
            track.status = status
            return "\nSuccessful modification\n"
    else:
        return "\nTrack not found\n"


# Procedure to delete a Track
def deleteTrack(number):
    for track in trackList:
        if number == track.number:
            trackList.remove(track)
            return "\nSuccessful delete\n"
    else:
        return "\nTrack no found\n"


# Procedure to add a gate in the Gate object
def addGate(number, status):
    newGate = MaintenanceGates(number, status)
    gateList.append(newGate)


# Procedure to verify the gate is not repeated
def verifyGate(number):
    for gate in gateList:
        if number == gate.number:
            return True
    else:
        return False


# Procedure to verify the gate of the flight exist
def verifyGateFlight(number):
    for gate in gateListFlight:
        if number == gate.number:
            return True
    else:
        return False


# Procedure to push in listGateFlight
def pushListGateFlight(number):
    for gate in gateList:
        if number == gate.number:
            gateListFlight.append(gate)


# Procedure to verify the plaen of the flight exist
def verifyPlaneFlight(model):
    for aircraft in aircraftListFlight:
        if model == aircraft.model:
            return True
    else:
        return False


# Procedure to push in listPlaneFlight
def pushListPlaneFlight(model):
    for aircraft in aircraftList:
        if model == aircraft.model:
            aircraftListFlight.append(aircraft)


# Procedure to show the Gate info
def showGates():
    if gateList != []:
        for gate in gateList:
            print("Gate number:", gate.number, "Gate status:", gate.status)
    else:
        print("\nNo gates found\n")


# Procedure to modify a gate
def modifyGate(number, status):
    for gate in gateList:
        if number == gate.number:
            gate.status = status
            return "\nSuccessful modification\n"
    else:
        return "\nGate not found\n"


# Procedure to delete a gate
def deleteGate(number):
    for gate in gateList:
        if number == gate.number:
            gateList.remove(gate)
            return "\nSuccesful delete\n"
    else:
        return "\nGate not found\n"


# Procedure to add a airline
def addAirline(name, foundationYear, type, operationCountries):
    newAirline = AirlineMaintenance(name, foundationYear, type, operationCountries)
    airlineList.append(newAirline)


# Procedure to verify a airline name is unique
def verifyAirline(name):
    for airline in airlineList:
        if name == airline.name:
            return True
    else:
        return False


# Procedure to show airline info
def showAirlines():
    if airlineList != []:
        for airline in airlineList:
            print("Name: ", airline.name, "Foundation Year: ", airline.foundationYear,
                  "Type: ", airline.type, "Number of countries where it operates: ", airline.operationCountries)
    else:
        print("\nNo airlines found\n")


# Procedure to modify a airline
def modifyAirline(name, foundationYear, type, operationCountries):
    for airline in airlineList:
        if name == airline.name:
            airline.foundationYear = foundationYear
            airline.type = type
            airline.operationCountries = operationCountries
            return "\nSuccessful modification\n"
    else:
        return "\nAirline not found\n"


# Procedure to delete a airline
def deleteAirline(name):
    for airline in airlineList:
        if name == airline.name:
            airlineList.remove(airline)
            return "\nSuccesful delete\n"
    else:
        return "\nAirline not found\n"


# Procedure to add a crew
def addCrewmember(name, age, id, airline, type, status):
    newCrewmbember = CrewMaintenance(name, age, id, airline, type, status)
    crewList.append(newCrewmbember)


# Procedure to verify the crew
def verifyCrewmember(id):
    for member in crewList:
        if id == member.id:
            return True
    else:
        return False


# Procedure to show the crew info
def showCrew():
    if crewList != []:
        for crew in crewList:
            print("Name: ", crew.name, "Age: ", crew.age, "Identification card: ", crew.id,
                  "Airline: ", crew.airline, "Type: ", crew.type, "Status: ", crew.status)
    else:
        print("\nCrew not found\n")


# Procedure to delete a crew
def deleteCrew(id):
    for crew in crewList:
        if id == crew.id:
            crewList.remove(crew)
            return "\nSuccesful delete\n"
    else:
        return "\nCrewmember not found\n"


# Procedure to modify
def modifyCrew(id, name, age, airline, type, status):
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


# Procedure to add
def addAircraft(model, creationyear, id, airline, capacity, status):
    newAircraft = PlaneMaintenance(model, creationyear, id, airline, capacity, status)
    aircraftList.append(newAircraft)


# Procedure to verify
def verifyAircraft(id):
    for aircraf in aircraftList:
        if id == aircraf.id:
            return True
    else:
        return False


# Procedure to show info
def showAircraft():
    if aircraftList != []:
        for aircraft in aircraftList:
            print("Model:", aircraft.model, "Creation year:", aircraft.creationyear,
                  "ID:", aircraft.id, "Airline:", aircraft.airline, "Capacity:", aircraft.capacity,
                  "Status:", aircraft.status)
    else:
        print("\nAircraft not found\n")


# Procedure to delete
def deleteAircraft(id):
    for aircraft in aircraftList:
        if id == aircraft.id:
            aircraftList.remove(aircraft)
            return "\nSuccesful delete\n"
    else:
        return "\nAircraft not found\n"


def modifyAircraft(id, model, creationyear, airline, capacity, status):
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
    pilot2 = pilotsList[i + 1].name
    costumersServer1 = costumersServerList[i].name
    costumersServer2 = costumersServerList[i + 1].name
    costumersServer3 = costumersServerList[i + 2].name
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
    pilotsList.clear()
    for crew in crewList:
        if crew.airline == airline and crew.status == "Available" and crew.type == "Pilot":
            pilotsList.append(crew)
    else:
        return False


def automaticCrewCostumerService(airline):
    costumersServerList.clear()
    for crew in crewList:
        if crew.airline == airline and crew.status == "Available" and crew.type == "Costumer service":
            costumersServerList.append(crew)
    else:
        return False


def getPilots():
    i = 0
    if pilotsList != []:
        x = "Names: {0} {1}".format(pilotsList[i].name, pilotsList[i + 1].name)
        for a in crewList:
            if a.name == pilotsList[i].name:
                a.status = "In service"
            elif a.name == pilotsList[i + 1].name:
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
            elif a.name == costumersServerList[i + 1].name:
                a.status = "In service"
            elif a.name == costumersServerList[i + 2].name:
                a.status = "In service"
        return costumersServerList[i].name + ", " + costumersServerList[i + 1].name \
               + " and " + costumersServerList[i + 2].name
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
                  "\nCrewCustomerService:", flight.crewCustomerService,
                  "\nPrice of the flight:", flight.price)
    else:
        print("\nFlights not found\n")


def deleteFlight(departureDate, departureTime, gate, plane):
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


def modifyFlight(departureDate, departureTime, departureDate2, departureTime2, timeFlight, departureAirport,
                 arrivalAirport):
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
                          "\nCrewCustomerService:", flight.crewCustomerService,
                          "\nPrice of the flight:", flight.price)
    else:
        print("No flights were found between those dates")


def secondReport(gate):  # This function looks for the number of flights that have a specific door
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
                  "\nCrewCustomerService:", flight.crewCustomerService,
                  "\nPrice of the flight:", flight.price)
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


def filterByTime():
    contFlights = 0
    times = []
    for flight in flightListFilter:
        times.append(flight.timeFlight)
    times.sort()
    for time in times:
        for flight in flightListFilter:
            if flight.timeFlight == time:
                contFlights = contFlights + 1
                print("\nInfo Flight" + "#:" + str(contFlights),
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
                      "\nCrewCustomerService:", flight.crewCustomerService,
                      "\nPrice of the flight:", flight.price)


def filterByPrice():
    contFlights = 0
    prices = []
    for flight in flightListFilter:
        prices.append(flight.price)
    prices.sort()
    for price in prices:
        for flight in flightListFilter:
            if flight.price == price:
                contFlights = contFlights + 1
                print("\nInfo Flight" + "#:" + str(contFlights),
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
                      "\nCrewCustomerService:", flight.crewCustomerService,
                      "\nPrice of the flight:", flight.price)


def filterByDate(decisionFilter, departureDate):
    contFlights = 0
    if decisionFilter == 1:
        for flight in flightListFilter:
            if flight.departureDate == departureDate:
                contFlights = contFlights + 1
                print("\nInfo Flight" + "#:" + str(contFlights),
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
                      "\nCrewCustomerService:", flight.crewCustomerService,
                      "\nPrice of the flight:", flight.price)
    else:
        print("There are no flights on that date")


def showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport):
    contFlights = 0
    roundTripDeparture = ""
    roundTripArrival = ""
    roundTripFlighsList = []
    if typeFlights == 1:
        for flight in flightList:
            if flight.departureAirport == departureAirport and flight.arrivalAirport == arrivalAirport:
                contFlights = contFlights + 1
                flightListFilter.append(flight)
                print("\nInfo Flight" + "#:" + str(contFlights),
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
                      "\nCrewCustomerService:", flight.crewCustomerService,
                      "\nPrice of the flight:", flight.price)
    elif typeFlights == 2:
        for flight in flightList:
            if flight.departureAirport == departureAirport and flight.arrivalAirport == arrivalAirport:
                roundTripDeparture = flight.departureAirport
                roundTripArrival = flight.arrivalAirport
                roundTripFlighsList.append(flight)
                flightListFilter.append(flight)
            elif flight.arrivalAirport == roundTripDeparture and flight.departureAirport == roundTripArrival:
                roundTripFlighsList.append(flight)
                flightListFilter.append(flight)
                for flight in roundTripFlighsList:
                    contFlights = contFlights + 1
                    print("\nInfo Flight" + "#:" + str(contFlights),
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
                          "\nCrewCustomerService:", flight.crewCustomerService,
                          "\nPrice of the flight:", flight.price)
        else:
            print("The return flight was not found")


def showFilterFlighs():
    contFlights = 0
    for flight in flightListFilter:
        contFlights = contFlights + 1
        print("\nInfo Flight" + "#:" + str(contFlights),
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
              "\nCrewCustomerService:", flight.crewCustomerService,
              "\nPrice of the flight:", flight.price)


def createTravel(departureAirport, arrivalAirport, gate, passenger):
    waitTime = '1'
    waitTime = datetime.strptime(waitTime, '%H')
    departure = departureAirport
    arrival = arrivalAirport
    flightTravel = []
    gate1 = gate
    layover = ""
    for flight3 in flightList:
        if flight3.departureAirport == departure and flight3.arrivalAirport == arrival and flight3.gate == gate1:
            Travel.addFlight(flight3, )
            flightTravel.append(flight3)
    for flight1 in flightTravel:
        for flight2 in flightList:
            if flight1.arrivalAirport == flight2.arrivalAirport:
                flightTravel.append(flight2)
                layover = flight2.arrivalAirport
    namePassenger = passenger
    newTravel = Travel(departure, arrival, layover, waitTime, namePassenger)
    travelList.append(newTravel)
    print(Travel.calculatePrice())
    print(Travel.calculateTimeFlight())
    Travel.showFlights()


def showInfoTravel():
    for travel in travelList:
        print("\nInfo Travel",
              "\nDeparture:", travel.departure,
              "\nArrival:", travel.arrival,
              "\nLayover:", travel.layover,
              "\nWait Time:", travel.waitTime,
              "\nTime Flight:", travel.timeFlight,
              "\nPrice:", travel.price,
              "\nPassenger:", travel.passenger,
              "\nFlights:", travel.showFlights())


def addTravel(passenger):
    for travel in travelList:
        if travel.passenger == passenger:
            newRecord = Record(passenger)
            Record.addTravel1(travel)
            recordList.append(newRecord)
            saveRecord(recordList)


def smartSearch(departureAirport, arrivalAirport, firstDate, secondDate, day):
    listDeparture = []
    listReturn = []
    listaprueba = []
    days = day
    date1 = firstDate
    date2 = secondDate
    date1Modify = datetime.strptime(date1, '%d/%m/%Y')
    result = date1Modify + timedelta(days=days)
    result2 = date1Modify - timedelta(days=days)
    date2Modify = datetime.strptime(date2, '%d/%m/%Y')
    result3 = date2Modify + timedelta(days=days)
    result4 = date2Modify - timedelta(days=days)


    for flight in flightList:
        if flight.departureAirport == departureAirport and flight.arrivalAirport == arrivalAirport:
            listaprueba.append(flight)
            date = datetime.strptime(flight.departureDate, '%d/%m/%Y')
            if result2 < date and date < result:
                listDeparture.append(flight)
            if result4 < date and date < result3:
                listReturn.append(flight)



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
                    while verifyGate(number) == True:
                        print("This gate already exist, try again")
                        number = input("Enter number of the gate")
                        if verifyGate(number) == False:
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
            print(modifyAircraft(id, model, creationYear, airline, capacity, status))

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
        if trackList != [] and gateList != [] and airlineList != [] and crewList != [] and airportList != [] \
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
                        timeFlight = input(
                            '\n Enter the time of flight ==> Example: "2:30" ==> Its two and a half hours')
                        datetime.strptime(timeFlight, '%H:%M')
                        break
                    except:
                        print("\n You have not entered a correct date")
                airportMenu()
                departureAirport = input("Enter the name of the airport which it belongs for the departure airport:")
                if verifyAirport(departureAirport) == False:
                    while verifyAirport(departureAirport) == False:
                        print("Airport doesn't exist, try again")
                        departureAirport = input(
                            "Enter the name of the airport which it belongs for the departure airport:")
                        if verifyAirport(departureAirport) == True:
                            break
                airportMenu()
                arrivalAirport = input("Enter the name of the airport which it belongs for the arrival airport:")
                if verifyAirport(arrivalAirport) == False:
                    while verifyAirport(arrivalAirport) == False:
                        print("Airport doesn't exist, try again")
                        arrivalAirport = input(
                            "Enter the name of the airport which it belongs for the arrival airport:")
                        while arrivalAirport == departureAirport:
                            print("Arrival and Departure are the same, try again")
                            arrivalAirport = input(
                                "Enter the name of the airport which it belongs for the arrival airport:")
                            if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                                break
                else:
                    while arrivalAirport == departureAirport or verifyAirport(arrivalAirport) == False:
                        print("Arrival and Departure are the same, try again")
                        arrivalAirport = input(
                            "Enter the name of the airport which it belongs for the arrival airport:")
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
                price = int(input("Enter the price of the flight:"))
                if airline != None and departureDate != None and departureTime != None and timeFlight != None and \
                        departureAirport != None and arrivalAirport != None and plane != None and gate != None and \
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
                pilotsList.clear()
                costumersServerList.clear()
                gateListFlight.clear()
                aircraftListFlight.clear()
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
                departureairport = input(
                    "Enter the name of the new airport which it belongs for the departure airport:")
                if verifyAirport(departureairport) == False:
                    while verifyAirport(departureairport) == False:
                        print("Airport doesn't exist, try again")
                        departureairport = input(
                            "Enter the name of the airport which it belongs for the departure airport:")
                        if verifyAirport(departureairport) == True:
                            break
                airportMenu()
                arrivalairport = input(
                    "Enter the correct name of the new airport which it belongs for the arrival airport:")
                if verifyAirport(arrivalairport) == False:
                    while verifyAirport(arrivalairport) == False:
                        print("Airport doesn't exist, try again")
                        arrivalairport = input(
                            "Enter the correct name of the airport which it belongs for the arrival airport:")
                        if verifyAirport(arrivalairport) == True and arrivalairport != departureairport:
                            break
                print(modifyFlight(departuredate, departuretime, departuredate2, departuretime2, timeflight,
                                   departureairport, arrivalairport))

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
    if role == 3:
        for flight in flightList:
            print(flight)


def decisionFilterPrices():
    print("\nDo you want to order by price?\n"
          "1)Yes.\n",
          "2)No.\n")
    option = input("Enter the action you want to do:")
    if option == "1":
        return 1
    elif option == "2":
        return 2
    else:
        print("Invalid option")
    decisionFilterPrices()


def decisionFilterTimes():
    print("\nDo you want to order by time of flight?\n"
          "1)Yes.\n",
          "2)No.\n")
    option = input("Enter the action you want to do:")
    if option == "1":
        return 1
    elif option == "2":
        return 2
    else:
        print("Invalid option")
    decisionFilterTimes()


def decisionFilterDates():
    print("\nDo you want to filter by date?\n"
          "1)Yes.\n",
          "2)No.\n")
    option = input("Enter the action you want to do:")
    if option == "1":
        return 1
    elif option == "2":
        return 2
    else:
        print("Invalid option")
    decisionFilterDates()


def travelDecision():
    print("\nDo you want create a travel?\n"
          "1)Yes.\n",
          "2)No.\n")
    option = input("Enter the action you want to do:")
    if option == "1":
        return 1
    elif option == "2":
        return 2
    else:
        print("Invalid option")
    travelDecision()


def travelMenu(role):
    if role == 3:
        role = 3
        print("\nCreation of Travel\n"
              "1)Start with the creation of the flight.\n",
              "2)Return Main Menu.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            print("These are the flights with which you have made filters")
            showFilterFlighs()
            print("We need some information about the flight you want to take, we will find the best option")
            departureAirport = input("Enter the name of the departure airport:")
            if verifyAirport(departureAirport) == False:
                while verifyAirport(departureAirport) == False:
                    print("Airport doesn't exist, try again")
                    departureAirport = input(
                        "Enter the name of the departure airport:")
                    if verifyAirport(departureAirport) == True:
                        break
            airportMenu()
            arrivalAirport = input("Enter the name of the arrival airport:")
            if verifyAirport(arrivalAirport) == False:
                while verifyAirport(arrivalAirport) == False:
                    print("Airport doesn't exist, try again")
                    arrivalAirport = input(
                        "Enter the name of the arrival airport:")
                    while arrivalAirport == departureAirport:
                        print("Arrival and Departure are the same, try again")
                        arrivalAirport = input(
                            "Enter the name of the arrival airport:")
                        if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                            break
            else:
                while arrivalAirport == departureAirport or verifyAirport(arrivalAirport) == False:
                    print("Arrival and Departure are the same, try again")
                    arrivalAirport = input(
                        "Enter the name of the arrival airport:")
                    if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                        break
            gate = input("Enter the number of gate")
            passengerName = input("Enter your name")
            createTravel(departureAirport, arrivalAirport, gate, passengerName)
            showInfoTravel()
            addTravel(passengerName)

        elif option == "2":
            return 2
        else:
            print("Invalid option")
        travelDecision()


def searchFlightsMenu(role):
    if role == 3:
        role = 3
        typeFlights = 0
        print("\nYou are in passenger mode\n"
              "\nAero-TEC\n",
              "1)One way flights.\n",
              "2)Roundtrip flights.\n",
              "3)Back.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            typeFlights = 1
            decisionFilterDate = 0
            decisionFilterPrice = 0
            decisionFilterTime = 0
            departureDate = ""
            airportMenu()
            departureAirport = input("Enter the name of the airport which it belongs for the departure airport:")
            if verifyAirport(departureAirport) == False:
                while verifyAirport(departureAirport) == False:
                    print("Airport doesn't exist, try again")
                    departureAirport = input(
                        "Enter the name of the airport which it belongs for the departure airport:")
                    if verifyAirport(departureAirport) == True:
                        break
            airportMenu()
            arrivalAirport = input("Enter the name of the airport which it belongs for the arrival airport:")
            if verifyAirport(arrivalAirport) == False:
                while verifyAirport(arrivalAirport) == False:
                    print("Airport doesn't exist, try again")
                    arrivalAirport = input(
                        "Enter the name of the airport which it belongs for the arrival airport:")
                    while arrivalAirport == departureAirport:
                        print("Arrival and Departure are the same, try again")
                        arrivalAirport = input(
                            "Enter the name of the airport which it belongs for the arrival airport:")
                        if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                            break
            else:
                while arrivalAirport == departureAirport or verifyAirport(arrivalAirport) == False:
                    print("Arrival and Departure are the same, try again")
                    arrivalAirport = input(
                        "Enter the name of the airport which it belongs for the arrival airport:")
                    if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                        break
            showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            decisionFilterDate = decisionFilterDates()
            if decisionFilterDate == 1:
                while True:
                    try:
                        departureDate = input('\n Enter the departure date ==> Example: "10/01/2000"')
                        datetime.strptime(departureDate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date, try again")
                filterByDate(decisionFilterDate, departureDate)
            else:
                showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            decisionFilterPrice = decisionFilterPrices()
            if decisionFilterPrice == 1:
                filterByPrice()
            else:
                showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            decisionFilterTime = decisionFilterTimes()
            if decisionFilterTime == 1:
                filterByTime()
            else:
                showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            Vtravel = travelDecision()
            if Vtravel == 1:
                travelMenu(role)
            else:
                flightListFilter.clear()
                searchFlightsMenu(role)
        elif option == "2":
            typeFlights = 2
            decisionFilterDate = 0
            decisionFilterPrice = 0
            decisionFilterTime = 0
            departureDate = ""
            airportMenu()
            departureAirport = input("Enter the name of the airport which it belongs for the departure airport:")
            if verifyAirport(departureAirport) == False:
                while verifyAirport(departureAirport) == False:
                    print("Airport doesn't exist, try again")
                    departureAirport = input(
                        "Enter the name of the airport which it belongs for the departure airport:")
                    if verifyAirport(departureAirport) == True:
                        break
            airportMenu()
            arrivalAirport = input("Enter the name of the airport which it belongs for the arrival airport:")
            if verifyAirport(arrivalAirport) == False:
                while verifyAirport(arrivalAirport) == False:
                    print("Airport doesn't exist, try again")
                    arrivalAirport = input(
                        "Enter the name of the airport which it belongs for the arrival airport:")
                    while arrivalAirport == departureAirport:
                        print("Arrival and Departure are the same, try again")
                        arrivalAirport = input(
                            "Enter the name of the airport which it belongs for the arrival airport:")
                        if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                            break
            else:
                while arrivalAirport == departureAirport or verifyAirport(arrivalAirport) == False:
                    print("Arrival and Departure are the same, try again")
                    arrivalAirport = input(
                        "Enter the name of the airport which it belongs for the arrival airport:")
                    if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                        break
            showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            decisionFilterDate = decisionFilterDates()
            if decisionFilterDate == 1:
                while True:
                    try:
                        departureDate = input('\n Enter the departure date ==> Example: "10/01/2000"')
                        datetime.strptime(departureDate, '%d/%m/%Y')
                        break
                    except:
                        print("\n You have not entered a correct date, try again")
                filterByDate(decisionFilterDate, departureDate)
            else:
                showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            decisionFilterPrice = decisionFilterPrices()
            if decisionFilterPrice == 1:
                filterByPrice()
            else:
                showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            decisionFilterTime = decisionFilterTimes()
            if decisionFilterTime == 1:
                filterByTime()
            else:
                showSearchFlightsAirport(typeFlights, departureAirport, arrivalAirport)
            Vtravel = travelDecision()
            if Vtravel == 1:
                travelMenu(role)
            else:
                flightListFilter.clear()
                searchFlightsMenu(role)
        elif option == "3":
            passengerMenu(role)
        else:
            print("Invalid option")
        searchFlightsMenu(role)


def smartSearchMenu(role):
    if role == 3:
        role = 3
        print("\nSmart Search of flights\n",
              "1)Smart Search\n",
              "2)Log Out\n")

        option = input("Enter the action you want to do:")
        if option == "1":
            airportMenu()
            departureAirport = input("Enter the name of the airport which it belongs for the departure airport:")
            if verifyAirport(departureAirport) == False:
                while verifyAirport(departureAirport) == False:
                    print("Airport doesn't exist, try again")
                    departureAirport = input(
                        "Enter the name of the airport which it belongs for the departure airport:")
                    if verifyAirport(departureAirport) == True:
                        break
            airportMenu()
            arrivalAirport = input("Enter the name of the airport which it belongs for the arrival airport:")
            if verifyAirport(arrivalAirport) == False:
                while verifyAirport(arrivalAirport) == False:
                    print("Airport doesn't exist, try again")
                    arrivalAirport = input(
                        "Enter the name of the airport which it belongs for the arrival airport:")
                    while arrivalAirport == departureAirport:
                        print("Arrival and Departure are the same, try again")
                        arrivalAirport = input(
                            "Enter the name of the airport which it belongs for the arrival airport:")
                        if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                            break
            else:
                while arrivalAirport == departureAirport or verifyAirport(arrivalAirport) == False:
                    print("Arrival and Departure are the same, try again")
                    arrivalAirport = input(
                        "Enter the name of the airport which it belongs for the arrival airport:")
                    if verifyAirport(arrivalAirport) == True and arrivalAirport != departureAirport:
                        break
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
            while True:
                try:
                    day = int(input("Enter the range of days you want to search the flight:"))
                    break
                except:
                    print("\n You have not entered a correct date, try again")

            smartSearch(departureAirport, arrivalAirport, firstDate, secondDate, day)

        elif option == "2":
            passengerMenu(role)

        else:
            print("Invalid option")
        smartSearchMenu(role)


def passengerMenu(role):
    if role == 3:
        role = 3
        print("\nYou are in passenger mode\n"
              "\nAero-TEC\n",
              "1)Search for flights.\n",
              "2)Smart Search.\n"
              "3)Log out.\n")
        option = input("Enter the action you want to do:")
        if option == "1":
            searchFlightsMenu(role)

        elif option == "2":
            smartSearchMenu(role)

        elif option == "3":
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
            flights(role)

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
          "3)Exit.\n")
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
        save(flightList)
        sys.exit()
    else:
        print("Invalid option")
    loginMenu()


def start():
    global flightList
    flightList = charge()
    loginMenu()
    global recordList
    recordList = charge1()


start()
