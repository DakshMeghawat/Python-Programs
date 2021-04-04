class Flight():
    fno =1
    price =200
    price=222
    source="daskss"
    dst="dasdsa"
    dptime="9.00 AM"
    date="04-05-21"
    tic=20
    left=20
    airline="jjdj"
    def fill(self,fno,price,source,dst,dptime,date,tic,left,airline):
        self.fno=fno
        self.price=price
        self.source=source
        self.dst=dst
        self.dptime=dptime
        self.date=date
        self.tic=tic
        self.left=left
        self.airline=airline
        
    def show(self):
        print()
        print()
        print("**********************************************************************************************************************************************")
        print()
        print()
        print("                                 Your Airline Is =>  ",self.airline)
        print("Flight Number => " ,self.fno,"        From =>",self.source," To  Destination => ",self.dst,"       Date => ",self.date,"      Price => ",self.price)
        print("No of Seats Available => ",self.left,)
       # print("Passenger Name => ",name,"        Age => ",age,"     Gender=> ",gender,"    Ticket Price Is => ",price,"Rs")
        print()
        print()
        print()
        print("**********************************************************************************************************************************************")
    def buy(self,name,age,Pno,Add,gender):
            self.name=name
            self.age=age
            self.Pno=Pno
            self.Add=Add
            self.gender=gender
            self.left=self.left - 1 
            
            print("**********************************************************************************************************************************************")
            print()
            print()
            print("                                 Your Airline Is =>  ",self.airline)
            print("Flight Number => " ,self.fno,"        From =>",self.source," To  Destination => ",self.dst,"       Date => ",self.date,"      Price => ",self.price)
            print("No of Seats Available => ",self.left,)
            print("Passenger Name=>  ",self.name ,"         Age =>  ",self.age,"        Gender=>",self.gender)
            print("Address => ",self.Add,"        Phone no =>  ",self.Pno)
       # print("Passenger Name => ",name,"        Age => ",age,"     Gender=> ",gender,"    Ticket Price Is => ",price,"Rs")
            print()
            print()
            print()
            print("**********************************************************************************************************************************************")
            print("Thanks For Visiting")
      
class Airlines(Flight):
    def __init__(self,Name,List):
        self.Name=Name
        self.List=List
    #f1=Flight(3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)
    #f2=Flight(4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
    
    

   # f1=Flight(3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)
    #f2=Flight(4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
choice=0
choice=int (input('''Press 1 to check all flights =>  
Press 2 to Buy Ticket  =>  '''))
f1=Flight()
f1.fill(3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30,"Indigo")
f2=Flight()
f2.fill(4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60,"Indigo")
Indigoflights=[]
Indigoflights.append(f1)
Indigoflights.append(f2)
IndigoAirline=Airlines("indigo",Indigoflights)
f3=Flight()
f3.fill(2689,4000,"Pune","Ahemdabad","12:00 PM","04-04-2021",150,150,"Jetairways")
f4=Flight()
f4.fill(6498,40000,"Delhi","Paris","2:00 PM","04-04-2021",150,150,"jetairways")
Jetflights=[]
Jetflights.append(f3)
Jetflights.append(f4)
f5=Flight()
f5.fill(5942,90000,"Delhi","Canada","8:00 AM ","06-04-2021",200,200,"Air India")
f6=Flight()
f6.fill(8641,5000,"Udaipur","Goa","6:00 PM","06-04-2021",150,150,"Air India")
AirIndiaflights=[]
AirIndiaflights.append(f5)
AirIndiaflights.append(f6)
AirIndiaAirline=Airlines("Air India",AirIndiaflights)
#Indigo=Airlines(1,3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)   
#AirIndia=Airlines(1,4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
#Jetairways=Airlines(1,5689,2000,"Udaipur","Delhi","1:00 PM","03-04-2021",120,120)
def show1():
    PName=input("Enter Your Name => ")
    Phone_No=int(input('''Please Enter The same  Phone Number Linked With Your Account  =>  '''))
    Address=input("Enter Your Address => ")
    Gender=input("Enter Your Gender => ")
    Accountno=input("Enter your Account Number => ")
    Age=input("Enter Your Age =>  ")
    Air=int(input(''' 
    
    
    Press 1 to Buy Indigo Ticket =>
    Press 2 to Buy Jet Airways Ticket => 
    Press 3 to Buy Air India Ticket =>  '''))
    src=input("Enter Your Destintion Where You Want To Go => ")

    if (Air==1):
       
        if (src=="USA"):
            f1.buy(PName,Age,Phone_No,Address,Gender)
        elif (src=="Pune"):
            f2.buy(PName,Age,Phone_No,Address,Gender)
        else :
            print("This Flight Is Not Available Kindly Choose From The Available Flights")    
    elif (Air==2):
        if (src=="Ahemdabad"):
            f3.buy(PName,Age,Phone_No,Address,Gender)
        elif (src=="Paris"):
            f4.buy(PName,Age,Phone_No,Address,Gender)
        else :
            print("This Flight Is Not Available Kindly Choose From The Available Flights")    
    elif (Air==3):
        if (src=="Canada"):
            f5.buy(PName,Age,Phone_No,Address,Gender)
        elif (src=="Goa") :
            f6.buy(PName,Age,Phone_No,Address,Gender) 
        else :
            print("This Flight Is Not Available Kindly Choose From The Available Flights")  
    else :
            print("This Flight Is Not Available Kindly Choose From The Available Flights")       
if (choice ==2):
    show1()
elif (choice ==1) :
    for i in Indigoflights:
        i.show()
        #print("In Progress")
    for i in Jetflights:
        print()
        print("**************************************************************************************************************************************************")
        print()
        i.show()
    for i in AirIndiaflights:
        print()
        print("**************************************************************************************************************************************************")
        print()
        i.show()
    A=0
    A=int(input('''Press 1 if you want to buy the flight
    
        IMPORTENT INSTRUCTION =>   Please Check The Destination Speling From The ticket Once And Write The Same Speling 
        As Written IN The Above Flight Information Only When Asked Otherwise You Will Not Able To Book Ticket  
              =>   '''))
    if(A==1):
        
        show1()
    else :
        print()
        print("***************************************************************************************************************************************************")
        print()
        print("Thanks For Visiting To Our Site ")


