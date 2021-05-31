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
                ch=input("Enter Your Account Number => ")
                pno=input("Enter your phone number")
                B=open("Num.txt","r")
                k=int(B.read())
                i=int(0)
                while (i<k):
                        n=lis[i]
                        p=n.split()
                        if (C==3):
                                S.sh(ch,p[0],p[1],p[2],p[3],p[4],p[5],i)
                        if (C==4):
                                if(ch==p[0] and pno==p[2]):
                                        S.modify(i)
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
                        for k in A:
                                lis.append(k)
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
                q=int(input('''Press 1 To Deposit In Your Account => 
                Press 2 To Withdraw Erom Your Account => '''))
                if (q==1):
                        import os
                        from time import sleep
                        _ =os.system('cls') 
                        A=int(input("Enter Amount you want to Deposit => "))
                        B=int(Z[i])
                        
                        B=B+A
                        
                        Z[i]=B
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
                        A=int(input("Enter Amount you want to withdraw => "))
                        B=int(Z[int(i)])
                        if(B>=A):
                                B=B-A
                                Z[i]=B
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
                        else:
                                import os
                                from time  import sleep
                                _ = os.system('cls') 
        #screen_clear()
                                print("Oops It Seems You Don't Have Enough Balance ..............")
                                print("Your Current Balance is => ",B,'\n',"And You Asked To Withdraw => ",A,'\n',"So You Cannot Withdraw More Than That")
                else:
                        print("Wrong input")
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
                        bal=input("Enter Amount To Be Depsited => ")
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
import os
from time import sleep
_ =os.system('cls') 
print("Welcome to the GOLDMINE Bank")
C=int(input('''Press 2 For Creating Account)
Press 3 For Log In Your Account
Press 4 To Withdraw And Deposit From Your Account
   =>  '''))
S=Saving_Account()
S.choice(C)  

