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



class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal) :
    def __init__(self, age, name):
        super().__init__(age, name)
    def bark(self):
        print(f"{self.name} is barking")
class Cat(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
    def sleep(self):
        print(f"{self.name} is a sleeping cat")

dog1 = Dog(9, "Jake")
dog1.bark()
dog1.eat()
cat1 = Cat(10, "kiko")
cat1.sleep()