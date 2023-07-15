#CHALLANGE - 1  SQUARE NUMBERS AND RETURN THEIR SUM

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self):
        print('sum of squared numbers:',self.x**2 + self.y**2 + self.z**2)
x = int(input("enter x value:"))
y = int(input("enter y value:"))
z = int(input("enter z value:"))
object1 = point(x,y,z)
print(object1.sqsum())


#CHALLANGE - 2  IMPLEMENT A CALCULATOR CLASS

class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
       return self.num1 * self.num2
    def divide(self):
        return self.num1 % self.num2
    
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
object_1 = calculator(num1,num2)
print('addition of num1 and num2:',object_1.add())
print('subtraction of num1 and num2:',object_1.subtract())
print('multipication of num1 and num2:',object_1.multiply())
print('division of num1 and num2',object_1.divide())


# CHALLANGE - 3  IMPLEMENT THE COMPLETE STUDENT CLASS

class Student:
    def _init_(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
name = input("enter the name:")
rollnumber = int(input("enter the rollnumber:"))
student = Student()
student.setName(name)
student.setRollNumber(rollnumber)
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)

#CHALLANGE - 4  IMPLEMENT A BANKING ACCOUNT

class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
class savingsaccount(Account):
    def __init__(self,title,balance,interest_rate):
        super().__init__(title,balance)
        self.interest_rate = interest_rate
title = input("enter the title:")
balance = int(input("enter the balance:"))
interest_rate = int(input("enter the interest rate:"))
account_2 = savingsaccount(title,balance,interest_rate)
print("account title:",account_2.title)
print("account balance:",account_2.balance)
print("account interest",account_2.interest_rate)




#CHALLANGE - 5  HANDLING A BANK ACCOUNT

class account:
    def __init__(self,balance):
        self.balance = balance
    def getbalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance += amount
    def withdrawal(self,amount):
        self.balance -= amount

class savingsaccount(account):
    def __init__(self,balance,interestrate):
        super().__init__(balance)
        self.interestrate = interestrate
    def interestAmount(self):
        return self.balance * (self.interestrate/100)
balance = int(input("enter balance amount:"))
deposit = int(input("enter deposit of amount:"))
balance_2 = int(input("enter the balance amount:"))
withdrawal = int(input("enter withdrawal:"))
interest_rate = int(input("enter the interest:"))
account_1 = account(balance)
account_1.deposit(deposit)
print('deposit of amount:',account_1.getbalance())
account_2 = account(balance_2)
account_2.withdrawal(withdrawal)
print('remaining amount:',account_2.getbalance())
account_interest = savingsaccount(balance_2,interest_rate)
print('total interest:',account_interest.interestAmount())