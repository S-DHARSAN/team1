import csv
from Availability import Room

class LogIn:
    def LogInPage():
        print("~"*50)
        print("\t\tLogin Page")
        print("~"*50)
        while 1:
            
            verify=0
            un=input("Enter your username:")
            pw=input("Enter your password:")

            with open('myCsv.csv','r') as file:
                myRead=csv.reader(file)
                for row in myRead:
                    if un==row[0] and pw==row[2] and un!="Username" and pw!="password":
                        print("***Login Successfully***")
                        Room.roomAvail()
                        verify=1
                        break
                if verify==0:
                    print("***Incorrect Username or password***")
                    continue
                        