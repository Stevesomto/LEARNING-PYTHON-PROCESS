# INHERITANCE allows a class to inherit attributes and methods from another class.
# This promotes code reusability and establishes a relationship between classes.
# keywords: base class, child, class, inheritance, super()

#PARENT CLASS
class Animal:
    def sound(self):
        print("Animal makes a sound")
#CHILD CLASS
class Dog(Animal):
    def sound(self):
        print("Dog barks")

#CHILD CLASS
class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
dog.sound()

class Parent:
    def display(self):
        print("This is the parent class.")
        
class Child(Parent):
    pass

child = Child()
child.display()