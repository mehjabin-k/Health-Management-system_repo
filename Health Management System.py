#Health Management System



#get current time and date
def getdate():
    """this function is use to get current time"""
    import datetime
    return datetime.datetime.now()

time1=getdate()

#client mehjabin function read and write in a file
def m_func1(p1,p2):
    """This function use for get client details and only for mehjabin"""
    if p2==1 :
        f=open("Mehjabin_Diet.text","a")
        f.write(str(p1))
        f.write("\n")
        f.write(input(" "))
        f.write("\n")
        f.write("*********************************************\n")
        f.close()
    else :

        f = open("Mehjabin_Exercise.txt", "a")
        f.write(str(p1))
        f.write("\n")
        f.write(input(" "))
        f.write("\n")
        f.write("*********************************************\n")

        f.close()
    print("You'r daily Report is here...\n")
    report = int(input("which report you want...\n 1 for Diet \n 2 for Exercise\n->>"))

    if report == 1:
        f = open("Mehjabin_Diet.text", "rt")
        for i in f:
            print(i, end=" ")
        f.close()
    else:
        f = open("Mehjabin_Exercise.txt", "rt")
        for i in f:
            print(i, end=" ")
        f.close()

#client sameer function read write function in file
def s_func1(p1,p2):
    """This function use for get client details and only for mehjabin"""
    if p2==1 :
        f=open("Sameer_Diet.text","a")
        f.write(str(p1))
        f.write("\n")
        f.write(input(" "))
        f.write("\n")
        f.write("*********************************************\n")
        f.close()
    elif p2==2:

        f = open("Sameer_Exercise.txt", "a")
        f.write(str(p1))
        f.write("\n")
        f.write(input(" "))
        f.write("\n")
        f.write("*********************************************\n")

        f.close()
    else:
        print("Wrong Input\try again..")


    print("You'r daily Report is here...\n")
    report = int(input("which report you want...\n 1 for Diet \n 2 for Exercise\n->>"))

    if report == 1:
        f = open("Sameer_Diet.text", "rt")
        for i in f:
            print(i, end=" ")
        f.close()
    elif report==2 :
        f = open("Sameer_Exercise.txt", "rt")
        for i in f:
            print(i, end=" ")
        f.close()
    else:
        print(" Unacceptable report request...")


#client harry function read and write in file
def h_func1(p1,p2):
    """This function use for get client details and only for harry"""
    if p2==1 :
        f=open("Harry_Diet.text","a")
        f.write(str(p1))
        f.write("\n")
        f.write(input(" "))
        f.write("\n")
        f.write("*********************************************\n")

        f.close()
    else:
        f = open("Harry_Exercise.txt", "a")
        f.write(str(p1))
        f.write("\n")
        f.write(input(" "))
        f.write("\n")
        f.write("*********************************************\n")

        f.close()
    print("You'r daily Report is here...\n")
    report = int(input("which report you want...\n 1 for Diet \n 2 for Exercise\n->>"))

    if report==1 :
        f=open("Harry_Diet.text","rt")
        for i in f:
            print(i,end=" ")
        f.close()
    else:
        f = open("Harry_Exercise.txt", "rt")
        for i in f:
            print(i, end=" ")
        f.close()

#here we ask to client, want to continue or else stop
play="y"
#i=0
print("WELCOME TO \r\t MK HELTH MANAGEMENT SYSTEM ")

name = input("\nPlease Enter You'r Name  : ")

while play=='y' or play=='Y':
    if name == "Mehjabin" or name == "mehjabin" or name == "Harry" or name == "harry" or name == "Sameer" or name == "sameer" :
        choice = int(input("Please Enter you choice...\n 1 for Diet\n 2 for Exercise\n->>"))
        print("Please Enter You'r Diet or Exercise : \n")
        if name == "Mehjabin" or name == "mehjabin":
            m_func1(time1, choice)
        elif name == "Harry" or name == "harry":
            h_func1(time1, choice)
        else:
            s_func1(time1, choice)
        play = input("Do you want to Re- Run then please enter Y or N : ")
        print("\n\t\tThank you for using HMS Software...")
    else:
        print("Sorry!!! You are not my client..\nSo Kindly talk to MK.\nMk Number : 1234562133 \n\t\tThank You!!!")

        break

