#Polymorhphism is phenomenon in which similar method gives different output#

class Animals:
    def speak(self):
        print("Animals will not speak")


class Humans:
    def speak(self):
        print("Humans will speak")


obj = Animals()
obj2 = Humans()

obj.speak()
obj2.speak()


#Types of Polymorhphism 

# 1.Method Overriding  (we need inheritance)


class Animal:
    a = 12
    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"your name is {self.name}")

class Humans(Animal):
    b = 12
    def details(self):
        super().details()
        print(f"your info is {self.name} and this is all we have")


obj = Humans("Sam")
obj.details()

#when we are doing inheritance and parent and child classes have same 
#method name so the child class method will override your parent class method 

#method overloading

class hello:
    def speak(self,a):
         
         print(f"how are you ")
    
    def speak(self,a,b):
         
        print("how are you ")

#Enscapsulation

class Factory:
    __name = "Mahindra" #Private class attribute

    def __init__(self,type, tyre, color):
        self.color = color #public object attribute
        self.tyre = tyre
        self.type = type

    def details(self): #public method
        print("Hello your details are: ")


class hello(Factory):
     print(Factory.__name)

obj = Factory("sedan", "MRF", "black")

print(obj.name)



class Hello:
    __a = 12

    @classmethod
    def info(cls):
        print(cls.__a)

obj = hello()

obj.info()


#Abstraction

from abc import ABC, abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass


class bike(enforce):
    def enginestart():
        pass

class car(enforce):
    def enginestart():
        pass

class truck(enforce):
    pass


obj1 = bike()
obj2 = car()
obj2 = truck()
