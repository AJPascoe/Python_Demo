# class Students:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
    
#     def getInfo(self):
#         print(f"{self.name} is {self.age} years old!")

# class Subject(Students):
#     def __init__(self, age, name, sub):
#         super().__init__(age, name)
#         self.sub = sub

#     def getInfo1(self): 
#         print(f"{self.name} is in {self.sub} class")




# student1 = Subject(16,"John", "Maths")
# student2 = Students(20,"Luke")
# student1.getInfo()
# student1.getInfo1()
# student2.getInfo()



# class Animal:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")
# class Dog(Animal) :
#     def __init__(self, age, name):
#         super().__init__(age, name)

#     def bark(self):
#         print(f"{self.name} is barking")

#     def age1(self):
#         print(f"{self.name} is {self.age} years old")
# class Cat(Animal):
#     def __init__(self, age, name):
#         super().__init__(age, name)

#     def sleep(self):
#         print(f"{self.name} is a sleeping cat")

#     def age1(self):
#         print(f"{self.name} is {self.age} years old")

# dog1 = Dog(9, "Jake")
# dog1.bark()
# dog1.eat()
# dog1.age1()
# cat1 = Cat(10, "kiko")
# cat1.sleep()
# cat1.age1()




# class polygon:
#     def display(self):
#         print("This text is from polygon - display")

#     def get_perimeter(self):
#         perimeter = sum(self.sides)
#         return perimeter

#     def __init__(self, sides):
#         self.sides=sides
# class triangle(polygon):
#     def display(self):
#         print("This text is from triangle - display")
#         super().display()


# obj1 = triangle([4,5,6])
# x = obj1.get_perimeter()
# print("The perimeter value is : ", x)
# obj1.display()

import  sys

class BankAccount:
    def __init__(self, pinNumber, balance=0):
        self.pinNumber = pinNumber
        self.balance = balance

    def start(self):
        
        while True:
            user = input("Which service do you require? \nd - Deposit \nw - Withdraw\nb - Balance\nc - Change Pin\nq - Quit\n\n")
            if user == "d":
                x = int(input("Deposit amount: "))
                self.add(x)
            elif user == "w":
                x = int(input("Withdraw amount: "))
                self.minus(x)
            elif user == "b":
                self.showBalance()
            elif user == "q":
                 sys.exit()
            elif user == "c":
                x = int(input("New Pin: "))
                self.change(x)
            else:
                print("Incorrect option \n")

    def change(self, newPin):
        self.pinNumber = newPin
        print(f"Your new pin number is : {self.pinNumber}")
        

    def showBalance(self):
        print(f"Your balance is: {self.balance}")

    def add(self, deposit):
        self.balance += deposit
        print(f"Bank Account Number {self.pinNumber} has £{self.balance}")
        user = input("Would you like a reciept? ")
        if user == "y":
            print(f"{self.balance}{self.balance}{self.balance}{self.balance}")
        else:
            pass
    
    def minus(self, withdraw):
        if withdraw > self.balance:
            print(f"You don't have enough cash! \nYour balance is {self.balance}")
        else:
            self.balance -= withdraw
            print(f"Bank Account Number {self.pinNumber} has £{self.balance}")
            user = input("Would you like a reciept? ")
            if user == "y":
                print(f"{self.balance}{self.balance}{self.balance}{self.balance}")
            else:
                pass

x = int(input("Enter Pin Number: "))
deposit1 = BankAccount(x)
# deposit1.add(10)
deposit1.start()


# deposit1 = BankAccount.add(10)