#CHALLANGE - 1  SQUARE NUMBERS AND RETURN THEIR SUM

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self):
        print('sum of squared numbers:',self.x**2 + self.y**2 + self.z**2)
object1 = point(1,3,5)
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
object_1 = calculator(10,94)
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

student_object = Student()
student_object.setName("michale")
student_object.setRollNumber(191231)
name = student_object.getName()
rollNumber = student_object.getRollNumber()
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

account_1 = Account("ashish",5000)
print(account_1.title)
print(account_1.balance)
account_2 = savingsaccount("ashish",5000,5)
print(account_2.title)
print(account_2.balance)
print(account_2.interest_rate)


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
account_1 = account(2000)
account_1.deposit(500)
print('deposit of amount:',account_1.getbalance())
account_2 = account(2000)
account_2.withdrawal(500)
print('remaining amount:',account_2.getbalance())
account_interest = savingsaccount(2000,5)
print('total interest:',account_interest.interestAmount())







  