#Num=input("Enter account number=>")
print("Welcome to the GOLDMINE Bank")
C=int(input('''Press 2 For Creating Account)
Press 3 For Log In Your Account 
   =>  '''))

    
class Saving_Account():
    def write(self,Name,Phone_No,address,Age,Gender):
            print("hii")
            self.Name=Name
            self.Phone_No=Phone_No
            self.address=address
            self.Age=Age
            self.Gender=Gender
            A=open("Account.txt", "a")
            
            A.write(st)
            Name=input("Enter your name")
            A.write(Name)
            
            A.write(Phone_No)
            
            A.write(Address)
           
            A.write(Age)
            
            A.write(Gender)
            
            A.close()
            print("###################################################################################################################################")
            print()
            print()
            print("Congratulation Your Account Is Created")
            print()
            print()
            print("###################################################################################################################################")
    def show():        
            print("Log in")
            f = open("Account.txt", "r") 
            print(f.read(Name))    

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
        S=Saving_Account()
        S.write(Name,Phone_No,Address,Age,Gender)
if(C==3):
        print("in Progress")
#A=open("Account.txt", "w")
#l=input("Enter account number=>")
#A.write(l)
#A.close()
#A=open("Account.txt","r")
#print ("Output of Readlines after appending")
#N=A.readlines()
#print(N)
#A.close()