#Num=input("Enter account number=>")
print("Welcome to the GOLDMINE Bank")
C=int(input('''Press 2 For Creating Account)
Press 3 For Log In Your Account 
   =>  '''))

    
class Saving_Account():
        def sh(self,ch,acc,Name,phone,Add,age,gender):
                self.acc=acc
                self.Name=Name
                self.phone=phone
                self.Add=Add
                self.age=age
                self.gender=gender
                self.ch=ch
                if (self.ch==self.acc):
                        print("Your Account Number Is => ",self.acc)
                        print("Your Name is => ",self.Add)
                        print("Your age is => ",self.age)
                        print("Your Gender is => ",self.gender)
                        print("Your Phone Number Is => ",self.phone)
        def write(self,Name,Phone_No,address,Age,Gender):
                
                print("hii")
                self.Name=Name
                self.Phone_No=Phone_No
                self.address=address
                self.Age=Age
                self.Gender=Gender
                A=open("Account.txt", "a")
            
                A.write(st+' ')
                Name=input("Enter your name")
                A.write(Name+' ')
            
                A.write(Phone_No+' ')
            
                A.write(Address+' ')
           
                A.write(Age+' ')
            
                A.write(Gender+'\n')
            
                A.close()
                print("###################################################################################################################################")
                print()
                print()
                print("Congratulation Your Account Is Created")
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
        def show():  
                
                print("Log in")
                f = open("Account.txt", "r") 
                print(f.read(Name))    
S=Saving_Account()
if (C==2):
        import random
        Accno = random.randint(100000000000, 999999999999)
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
        
        S.write(Name,Phone_No,Address,Age,Gender)
if(C==3):
        print("in Progress")
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
                S.sh(ch,p[0],p[1],p[2],p[3],p[4],p[5])
                i=i+1
                print(i)

        
       
#A=open("Account.txt", "w")
#l=input("Enter account number=>")
#A.write(l)
#A.close()
#A=open("Account.txt","r")
#print ("Output of Readlines after appending")
#N=A.readlines()
#print(N)
#A.close()