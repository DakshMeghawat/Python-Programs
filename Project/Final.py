var=0

src ="ddd"
class Saving_Account():
        
        def Search(self,C):
                f=open("Account.txt",'r')
                lis=[]
                for i in f:
                        lis.append(i)
                
                
                f.close()
                import os
                from time import sleep
                _ =os.system('cls')
                #print("IN search fun")
                ch=input("Enter Your Account Number => ")
                B=open("Num.txt","r")
                k=int(B.read())
                i=int(0)
                while (i<k):
                        n=lis[i]
                        p=n.split()
                        if (C==3):
                                S.sh(ch,p[0],p[1],p[2],p[3],p[4],p[5],i)
                        elif (C==4 or C==5):
                                print("in loop 1")
                                if(ch==p[0]):
                                        print("in loop 2")
                                        Val=S.modify(i)
                                        return(Val)
                        else:
                                import os 
                                from time import sleep
                                _=os.system('cls')
                                print("Oop Wrong Account Number \n")
                                print("Transaction End ")
                                end1()
                        i=i+1
                        #print(i)
        
        def sh(self,ch,acc,Name,phone,Add,age,gender,i):
                self.acc=acc
                self.Name=Name
                self.phone=phone
                self.Add=Add
                self.age=age
                self.gender=gender
                self.ch=ch
                self.i=i
                if (self.ch==self.acc):
                        import os
                        from time  import sleep
                        _ = os.system('cls') 
        #screen_clear()
                        print()
                        print()
                        print("**************************************************************************************************************************")
                        print()
                        print()
                        print("                                                GOLDMINE BANK")
                        print('____________________________________________________________________________________________________________________________')
                        print()
                        print("     Account Number  => ",self.acc,"                                                   Phone Number  => ",self.phone)
                        print()
                        print("_____________________________________________________________________________________________________________________________")
                        print()
                        print("     Name  => ",self.Name,"                  age => ",self.age,"                       Gender => ",self.gender)
                        A=open("Balance.txt",'r')
                        lis=[]
                        for l in A:
                                lis.append()
                        A.close()
                        print()
                        print("____________________________________________________________________________________________________________________________")
                        print()
                        print("Your Current Balance Is => ",lis[i])
                        print()
                        print("_____________________________________________________________________________________________________________________________")
                        A.close()
        def write(self,st,Name,Phone_No,address,Age,Gender,bal):
                
                print("hii")
                self.Name=Name
                self.Phone_No=Phone_No
                self.address=address
                self.Age=Age
                self.Gender=Gender
                self.st=st
                A=open("Account.txt", "a")
            
                A.write(st+' ')
                #Name=input("Enter your name")
                A.write(Name+' ')
            
                A.write(Phone_No+' ')
            
                A.write(address+' ')
           
                A.write(Age+' ')
            
                A.write(Gender+'\n')
            
                A.close()
                B=open("Balance.txt","a")
                D=open("Num.txt","r")
                F=int(D.read())
                if (F!=0):
                        B.write('\n')
                B.write(bal)
                B.close()
                D.close()
                import os
                from time import sleep
                _ =os.system('cls')
                print("###################################################################################################################################")
                print()
                print()
                print("Congratulation ",self.Name," Your Account Is Created")
                print()
                print()
                print("###################################################################################################################################")
                B=open("Num.txt","r+")
                c=int(B.read())
                B.close()
                B=open("Num.txt","w")
                c=c+1
                B.write(str(c))
                B.close()
        
        def modify(self,i):
                global src
                print(i)
                self.i=i
                s=i
                Z=[]  
                a=open("Balance.txt","r")
                
                for h in a:
                        Z.append(h)
                        
                a.close()
                import os
                from time import sleep
                _ =os.system('cls') 
                print("in loop 2")
                if(var==1):
                        q=int(input('''Press 1 To Deposit In Your Account => 
                Press 2 To Withdraw Erom Your Account => '''))
                        if (q==1):
                                import os
                                from time import sleep
                                _ =os.system('cls') 
                                A=int(input("Enter Amount you want to Deposit => "))
                                B=int(Z[i])
                        
                                B=B+A
                        
                                Z[i]=str(B)+'\n'
                                import os
                                from time import sleep
                                _ =os.system('cls')
                                print("Your Transaction Is Completed ")
                                print("Now Your Current Amount Is => ",Z[i])
                                C=open("Balance.txt","w")
                
                                for p in Z:
                                        C.write(str(p))
                                        F=open("Num.txt",'r')
                        
                                C.close()
                        elif (q==2):
                                import os
                                from time import sleep
                                _ =os.system('cls')        
                                A=int(input("Enter Amount you want to withdraw =>  "))
                                B=int(Z[i])
                                if(B>=A):
                                        B=B-A
                                        Z[i]=str(B)+'\n'
                                        import os
                                        from time import sleep
                                        _ =os.system('cls')
                                        print("Your Transaction Is Completed ")
                                        print("Now Your Current Amount Is => ",Z[i])
                                        #C=open("Balance.txt","w")
                
                                        for p in Z:
                                                C=open("Balance.txt","w")
                                                C.write(str(p))
                                                F=open("Num.txt",'r')
                        
                                        C.close()
                                else:
                                        import os
                                        from time  import sleep
                                        _ = os.system('cls') 
        #screen_clear()
                                        print("Oops It Seems You Don't Have Enough Balance ..............")
                                        print("Your Current Balance is => ",B,'\n',"And You Asked To Withdraw => ",A,'\n',"So You Cannot Withdraw More Than That")
                        else:
                                print("Wrong input")
                if (var==0):
                        
                        import os
                        from time import sleep
                        _ =os.system('cls')
                        
                        if(src=="USA"):
                                A=int(90000)
                        elif(src=="Pune"):
                                A=int(4000)
                        elif(src=="Ahmdabad"):
                                A=int(4000)
                        elif(src=="Paris"):
                                A=int(40000)
                        elif(src=="Canada"):
                                A=int(90000)
                        elif(src=="Goa"):
                                A=int(5000)
                        
                        #A=int(4000)
                        #print("Value of src is =>  ",src) 
                        #print("Value of A is => ",A)     
                        #q=input("Check  => ")
                        #A=int(input("Enter Amount you want to withdraw => "))
                        B=int(Z[i])
                        if(B>=A):
                                
                                gar=input(" ")
                                B=B-A
                                Z[i]=str(B)+'\n'
                                import os
                                from time import sleep
                                _ =os.system('cls')
                                print("Your Transaction Is Completed ")
                                print("Now Your Current Amount Is =>  ",Z[i])
                                gar=input(" Press Enter To Proceed ")
                                C=open("Balance.txt","w")
                
                                for p in Z:
                                        #C=open("Balance.txt","w")
                                        C.write(str(p))
                                        F=open("Num.txt",'r')
                        
                                C.close()
                                return (0)
                        else:
                                import os
                                from time  import sleep
                                _ = os.system('cls') 
        #screen_clear()
                                print("Oops It Seems You Don't Have Enough Balance ..............")
                                print("Your Current Balance is => ",B,'\n',"And You Asked To Withdraw => ",A,'\n',"So You Cannot Withdraw More Than That")
                                return(1)
        #def show():  
        #       f = open("Account.txt", "r") 
        #       print(f.read(Name))
        
        def choice(self,C):
                self.C=C
                import os
                from time import sleep
                _ =os.system('cls')   
                if (C==2):
                        import random
                        Accno = random.randint(100, 999)
                        print(Accno)
                        st=""
                        st=str(Accno)
                        print(type(st))
                        Name=input("Enter your name")
                        Phone_No=input("Enter your phone number")
                        Address=input("Enter your address")
                        Age=input("Enter your age")
                        Gender=input("Enter your gender")
                        
                        import os
                        from time import sleep
                        _ =os.system('cls')
                        bal=input("Enter Amount To Be Depsited =>  ")
                        import os
                        from time import sleep
                        _ =os.system('cls')
                        print()
                        print()
                        print("___________________________________________________________________________________________________________________________________")
                        print()
                        print("Your Account Number is",Accno)
                        print()
                        print("___________________________________________________________________________________________________________________________________")
                        S.write(st,Name,Phone_No,Address,Age,Gender,bal)
                elif(C==3):
                        S.Search(C)
                elif(C==4):
                        S.Search(C)
                else:
                        #_ =os.system('cls')
                        print("Sorry This option Is Not Available ") 
flag=0
Cname=0  
class Flight(Saving_Account):
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
            import os
            from time import sleep
            _ =os.system('cls')
            print("**********************************************************************************************************************************************")
            print()
            print()
            print("                                               Your Airline Is =>  ",self.airline)
            print()
            print("______________________________________________________________________________________________________________________________________________")
            print()
            print("Flight Number => " ,self.fno,"                From =>",self.source,"                To  Destination => ",self.dst,"                 Date => ",self.date)
            print()
            print("______________________________________________________________________________________________________________________________________________")
            print()
            print("Address => ",self.Add ,"          Price => ", self.price,"             Phone no =>  ",self.Pno)
            print()
            print("______________________________________________________________________________________________________________________________________________")
            print()
            print("Passenger Name=>  ",self.name ,"              Age =>  ",self.age,"                    Gender=>",self.gender)
            print()
            print("______________________________________________________________________________________________________________________________________________")
            print()
            print("Address => ",self.Add)
            print()
            print("______________________________________________________________________________________________________________________________________________")
            print()
       # print("Passenger Name => ",name,"        Age => ",age,"     Gender=> ",gender,"    Ticket Price Is => ",price,"Rs")
            print()
            print()
            print()
            print("**********************************************************************************************************************************************")
            print()
            print()
            print()
            print()
            print("Thanks For Visiting")
      
class Airlines(Flight):
    def __init__(self,Name,List):
        self.Name=Name
        self.List=List
Cname=int(0)
import os
from time import sleep
_ =os.system('cls')

# Program Starts From here


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
S=Saving_Account()

def show1():
        import os
        from time import sleep
        _ =os.system('cls')
        PName=input("Enter Your Name =>  ")
        Phone_No=int(input('''Please Enter The same  Phone Number Linked With Your Account  =>  '''))
        Address=input("Enter Your Address =>  ")
        Gender=input("Enter Your Gender => ")
        #Accountno=input("Enter your Account Number => ")
        Age=input("Enter Your Age =>  ")
        import os
        from time import sleep
        _ =os.system('cls')
        
        if (flag==0):
                Air=int(input(''' 
                Press 1 to Buy Indigo Ticket =>
                Press 2 to Buy Jet Airways Ticket => 
                Press 3 to Buy Air India Ticket =>  '''))
                global src
                src=input("Enter Your Destintion Where You Want To Go =>  ")
                print(src)
                if (Air==1):
                        if (src=="USA"):
                                num=5
                                Val=S.Search(num)
                        elif (src=="Pune"):
                                num=5
                                Val=S.Search(num)
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights") 
                                end1()   
                elif (Air==2):
                        if (src=="Ahemdabad"):
                                num=5
                                Val=S.Search(num)
                        elif (src=="Paris"):
                                num=5
                                Val=S.Search(num)
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights")  
                                end1()  
                elif (Air==3):
                        if (src=="Canada"):
                                num=5
                                Val=S.Search(num)
                        elif (src=="Goa") :
                                num=5
                                Val=S.Search(num)
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights") 
                                end1()
                if(Val==0):
                        if (Air==1):
                                if (src=="USA"):
                                        f1.buy(PName,Age,Phone_No,Address,Gender)
                                elif (src=="Pune"):
                                        f2.buy(PName,Age,Phone_No,Address,Gender)
                                else :
                                        print("This Flight Is Not Available Kindly Choose From The Available Flights")    
                                        end1()
                        elif (Air==2):
                                if (src=="Ahemdabad"):
                                        f3.buy(PName,Age,Phone_No,Address,Gender)
                                elif (src=="Paris"):
                                        f4.buy(PName,Age,Phone_No,Address,Gender)
                                else :
                                        print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                        end1()    
                        elif (Air==3):
                                if (src=="Canada"):
                                        f5.buy(PName,Age,Phone_No,Address,Gender)
                                elif (src=="Goa") :
                                        f6.buy(PName,Age,Phone_No,Address,Gender) 
                                else :
                                        print("This Flight Is Not Available Kindly Choose From The Available Flights") 
                                        end1() 
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                end1()
        elif(flag==1):
                if(Cname==1):
                        Air=1
                elif(Cname==2):
                        Air=2
                else:
                        Air=3    
                src = input("Enter Your Destintion Where You Want To Go =>  ")

                if (Air==1):
                        if (src=="USA"):
                                num=5
                                Val=S.Search(num)
                        elif (src=="Pune"):
                                num=5
                                Val=S.Search(num)
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights") 
                                end1()   
                elif (Air==2):
                        if (src=="Ahemdabad"):
                                num=5
                                Val=S.Search(num)
                        elif (src=="Paris"):
                                num=5
                                Val=S.Search(num)
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights") 
                                end1()   
                elif (Air==3):
                        if (src=="Canada"):
                                num=5
                                Val=S.Search(num)
                        elif (src=="Goa") :
                                num=5
                                Val=S.Search(num)
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                end1()  
                else :
                        print("This Flight Is Not Available Kindly Choose From The Available Flights")
                        end1()
                
                if(Val==0):
                        if (Air==1):
                                if (src=="USA"):
                                        f1.buy(PName,Age,Phone_No,Address,Gender)
                                elif (src=="Pune"):
                                        f2.buy(PName,Age,Phone_No,Address,Gender)
                                else :
                                        print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                        end1()    
                        elif (Air==2):
                                if (src=="Ahemdabad"):
                                        f3.buy(PName,Age,Phone_No,Address,Gender)
                                elif (src=="Paris"):
                                        f4.buy(PName,Age,Phone_No,Address,Gender)
                                else :
                                        print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                        end1()    
                        elif (Air==3):
                                if (src=="Canada"):
                                        f5.buy(PName,Age,Phone_No,Address,Gender)
                                elif (src=="Goa") :
                                        f6.buy(PName,Age,Phone_No,Address,Gender) 
                                else :
                                        print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                        end1()  
                        else :
                                print("This Flight Is Not Available Kindly Choose From The Available Flights")
                                end1()
        
def end1():
        
        print()
        print("***************************************************************************************************************************************************")
        print()
        print("Thanks For Visiting To Our Site ")
        print()
        print("***************************************************************************************************************************************************")
        print()
        print()
        exit()  
if (choice ==2):
    show1()
elif (choice ==1) :
    import os
    from time import sleep
    _ =os.system('cls')
    Filter=int(input("Press 1 to check particular company flights or Press 2 to check all the flights => "))
    if (Filter==1):
        flag=1
        Cname=int(input(''' 
                    Press 1 to check Indigo Ticket =>
                    Press 2 to check Jet Airways Ticket => 
                    Press 3 to check Air India Ticket =>  '''))
        if (Cname==1):
            for i in Indigoflights:
                print()
                print()
                i.show()
                print()
                print()
                print("**************************************************************************************************************************************************")
                print()
                print()
        if(Cname==2):
            for i in Jetflights:
                print()
                print()
                i.show()
                print()
                print("**************************************************************************************************************************************************")
                print()
                print()
                print()
        if(Cname==3):
            for i in AirIndiaflights:
                print()
                print()
                i.show()
                print()
                print("**************************************************************************************************************************************************")
                print()
    elif (Filter==2):
        for i in Indigoflights:
            print()
            print()
            i.show()
            print()
            print()
            print("**************************************************************************************************************************************************")
            print()
            print()
        #print("In Progress")
        for i in Jetflights:
            print()
            print()
            i.show()
            print()
            print("**************************************************************************************************************************************************")
            print()
            print()
            print()
        for i in AirIndiaflights:
            print()
            print()
            i.show()
            print()
            print("**************************************************************************************************************************************************")
            print()
    else:
        print("Wrong Choice")
    A=0
    A=int(input('''Press 1 if you want to buy the flight
    
        IMPORTENT INSTRUCTION =>   Please Check The Destination Speling From The ticket Once And Write The Same Speling 
        As Written IN The Above Flight Information Only When Asked Otherwise You Will Not Able To Book Ticket  
              =>   '''))
    import os
    from time import sleep
    _ =os.system('cls')
    if(A==1):
            
            show1()
    else :
            end1()



