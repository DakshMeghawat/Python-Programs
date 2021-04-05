#Num=input("Enter account number=>")
class Saving_Account():
        
        def Search(self,C):
                f=open("Account.txt",'r')
                lis=[]
                for i in f:
                        lis.append(i)
                
           
                f.close()
                ch=input("Enter Your Account Number => ")
                B=open("Num.txt","r")
                k=int(B.read())
                i=int(0)
                while (i<k):
                        n=lis[i]
                        p=n.split()
                        if (C==3):
                                S.sh(ch,p[0],p[1],p[2],p[3],p[4],p[5],i)
                        if (C==4):
                                if(ch==p[0]):
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
                        print("Your Account Number Is => ",self.acc)
                        print("Your Name is => ",self.Add)
                        print("Your age is => ",self.age)
                        print("Your Gender is => ",self.gender)
                        print("Your Phone Number Is => ",self.phone)
                        A=open("Balance.txt",'r')
                        print("Your Current Balance Is => ",A.readlines()[int(i)])
                        A.close()
        def write(self,Name,Phone_No,address,Age,Gender,bal):
                
                print("hii")
                self.Name=Name
                self.Phone_No=Phone_No
                self.address=address
                self.Age=Age
                self.Gender=Gender
                A=open("Account.txt", "a")
            
                A.write(st+' ')
                #Name=input("Enter your name")
                A.write(Name+' ')
            
                A.write(Phone_No+' ')
            
                A.write(Address+' ')
           
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
                c=c+1;
                B.write(str(c))
                B.close()
        def ckeck(slef,i):
                print("modify")
                B=open("Balance.txt","r")
                Print("Your Current Balance is => ")
                print(B.readlines()[int(i)])
                B.close()
        def modify(self,i):
                print(i)
                self.i=i
                s=i
                Z=[]  
                a=open("Balance.txt","r")
                #f=open("Num.txt","r")
                #w=int(f.read())
                #j=int(0)
                for h in a:
                        #print("Value Of J is => ",j)
                        Z.append(h)
                        #print("Value of K is => ",k)
                        #Z.append(k)
                        #print(Z[1])
                        #j=j+int(1)
                a.close()
                #f.close()
                M=Z
                print (M)
                #L=M.split()
                A=int(input("Enter Amount you want to withdraw => "))
                #print("Value of I is => ",i)
                #print("Value Of L Is => ",L)
                if (int(i)==0):
                        B=int(M[i])
                else :
                        s=s+1
                        B=int(M[s])
                print("check => ",B)
                B=B-A
                print("Value of Z is ",Z[i])
                Z[i]=B
                Z.pop()
                print("Z looks Like => ",Z)
                print("cur am => ",Z[i])
                C=open("Balance.txt","w")
                o=int(0)
                for p in Z:
                        C.write(str(p))
                        F=open("Num.txt",'r')
                        t=int(F.read())-1
                        if(o<t):
                                C.write('\n')
                        o=o+int(1)
                C.close()
                #self.i=i
                #B=open("Num.txt","r")
                #k=int(B.read())
                #D=[]
                #for j in D:
                #       D.append(j);
                #M=D.split()
                #print("Your balance is => ")
                #p=int(0)
                #while (p<k):
                        #M=D[p]
                        #L=M.split()
                #am=int(input("Enter the Ammout You Want to Withdraw => "))
                #B=open("Balance.txt","r")
                #print(self.i)
                #c=int(B.readlines()[self.i])
                #print("Your Balance is => ",c)
                #B.close()
                #B=open("Balance.txt","a")
                #for j in B:
                        #if (c==j):
                                #print("in it => ",c,"    ",j)
                                #am=c-am
                                #print(am)
                                #B.write(str(am))
                                #print("Your Balance is => ",am)
        def show():  
                
                print("Log in")
                f = open("Account.txt", "r") 
                print(f.read(Name)) 
print("Welcome to the GOLDMINE Bank")
C=int(input('''Press 2 For Creating Account)
Press 3 For Log In Your Account 
   =>  '''))   
S=Saving_Account()
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
        print("Your Account Number is",Accno)
        bal=input("Enter Amount To Be Depsited => ")
        S.write(Name,Phone_No,Address,Age,Gender,bal)
if(C==3):
        S.Search(C)
if(C==4):
        S.Search(C)
if(C==5):
        a=open("Balance.txt","r")
        d=a.readlines()
        print(d)
        #for v in a:
                #d.append(v)
        #print (d)    
        #print(a.readlines()[0])
        #a.write("900000")
        #print("Now  => ",a.readlines()[0])  
        #a.close()
      
#A=open("Account.txt", "w")
#l=input("Enter account number=>")
#A.write(l)
#A.close()
#A=open("Account.txt","r")
#print ("Output of Readlines after appending")
#N=A.readlines()
#print(N)
#A.close()