#CHALLANGE - 1  SQUARE NUMBERS AND RETURN THEIR SUM

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self):
        print('sum of squared numbers:',self.x**2 + self.y**2 + self.z**2)
x = int(input())
y = int(input())
z = int(input())
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
object_1 = calculator(10,94)
print('addition of num1 and num2:',object_1.add())
print('subtraction of num1 and num2:',object_1.subtract())
print('multipication of num1 and num2:',object_1.multiply())
print('division of num1 and num2',object_1.divide())


# CHALLANGE - 3  IMPLEMENT THE COMPLETE STUDENT CLASS

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
num1 = int(input())
num2 = int(input())
object_1 = calculator(num1,num2)
print('addition of num1 and num2:',object_1.add())
print('subtraction of num1 and num2:',object_1.subtract())
print('multipication of num1 and num2:',object_1.multiply())
print('division of num1 and num2',object_1.divide())


#CHALLANGE - 4  IMPLEMENT A BANKING ACCOUNT

class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
class savingsaccount(Account):
    def __init__(self,title,balance,interest_rate):
        super().__init__(title,balance)
        self.interest_rate = interest_rate
title = input()
balance = int(input())
interest_rate = int(input())
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
balance = int(input())
deposit = int(input())
balance_2 = int(input())
withdrawal = int(input())
account_1 = account(balance)
account_1.deposit(deposit)
interest_rate = int(input())
print('deposit of amount:',account_1.getbalance())
account_2 = account(balance_2)
account_2.withdrawal(withdrawal)
print('remaining amount:',account_2.getbalance())
account_interest = savingsaccount(balance_2,interest_rate)
print('total interest:',account_interest.interestAmount())
