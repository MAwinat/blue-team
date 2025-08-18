"""
mylist=[]
my1list=[]
for x in range(20):
    if x%2==0:
      mylist.append(x)
    else:
      my1list.append(x)"""
#print("This is even numbers: " ,mylist)    
#print("and this is for odd numbers " , my1list)     

"""
class Pirson:
  def __init__(self,name,age,city):
    self.name = name
    self.age = age
    self.city = city
  def full_name(self):
    #print(f"Hi, I'm {self.name}, {self.age} Years old  from , {self.city}.")
    return f"Hi, I'm {self.name}, {self.age} Years old  from , {self.city}."
   

my_name = Pirson("mohamed", 23, "misurata")


print(my_name.full_name()) """
#print(my_name.name)
#print(my_name.age)
#print(my_name.city)


class BankAccount:
  def __init__(self,owner, balance):
    self.owner = owner
    self.balance = balance
  def display(self):
    print(self.owner,self.balance)
  def Deposit(self,amount):
    self.balance += amount 
  def withdrow (self,value):
     if value > self.balance:
       raise ValueError
     else:
       self.balance = self.balance - value

account1 = BankAccount("mohamed",1000) 
account1.display()
account1.Deposit(10)
account1.display()
account1.withdrow(10)
account1.display()
