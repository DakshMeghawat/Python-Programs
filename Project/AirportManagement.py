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
        
class Airlines(Flight):
    def __init__(self,Name,List):
        self.Name=Name
        self.List=List
    #f1=Flight(3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)
    #f2=Flight(4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
    
    def buy(self,choice,name,age,gender):
        if (choice ==1):
            f1=Flight(3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)
            print("Passenger Name => ",name,"        Age => ",age,"     Gender=> ",gender)
        else:
            f2=Flight(4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
            print("Passenger Name => ",name,"        Age => ",age,"     Gender=> ",gender)

   # f1=Flight(3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)
    #f2=Flight(4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
choice=0
choice=int (input("Press 1 to check all flights =>  "))
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
#Indigo=Airlines(1,3271,90000,"Delhi","USA","9:00 AM"," 03-04-2021 ",30,30)   
#AirIndia=Airlines(1,4651,5000,"Delhi","Pune","9:00 AM"," 03-04-2021 ",60,60)
#Jetairways=Airlines(1,5689,2000,"Udaipur","Delhi","1:00 PM","03-04-2021",120,120)
if (choice ==1):
    Indigo.show()
    AirIndia.show()
    Jetairways.show()
elif (choice ==0) :
    for i in Indigoflights:
        i.show()
        #print("In Progress")
    for i in Jetflights:
        print()
        print("**************************************************************************************************************************88")
        print()
        i.show()


