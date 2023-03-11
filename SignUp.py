from LogIn import LogIn
import re
import csv

class SignUp:
    def signUpPage():
        print("-"*50)
        print("\t\tSignUp Page")
        print("-"*50)
        while 1:
            #verify username
            uName=0
            uNumber=0
            uPass=0
            verify=0
            userName=input("Enter your username:")

            with open('myCsv.csv','r') as file: 
                for row in file:
                    rows=row.split(",")
                    if rows[0]==str(userName):
                        print("***This User name is already exist try with other username***")
                        verify=1
                        break
                
                if verify==1:
                    continue
                else:
                    uName=1
            
            #verify phone number
            phoneNum=int(input("Enter your phone number:"))
            verify=0
            if phoneNum > 6000000000 and phoneNum < 10000000000 and phoneNum!=6666666666 and phoneNum!=7777777777 and phoneNum!=8888888888 and phoneNum!=9999999999:
                with open('myCsv.csv','r') as f:
                    for row in f:
                        rows=row.split(",")
                        if rows[1]==str(phoneNum):
                            verify=1
                            break

                    if verify==1:
                        print("This phone number is already exist try with other phone number")
                        continue
                    else:
                        uNumber=1
            else:
                print("***Invalid Phone Number***")
                continue


            #verify password
            __password=input("Enter your password:")
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
            match = re.compile(reg)
            res = re.search(match, __password)
            if res:
                uPass=1
                break
            else:
                print("Invalid Password")
                continue


        if uName ==1 and uNumber == 1 and uPass == 1:
            with open('myCsv.csv','a') as file:
                myWriter=csv.writer(file)
                myWriter.writerow([userName,phoneNum,__password])

            print("***SignUp Succcessfully***")
            #print(detailsList)
            LogIn.LogInPage()
