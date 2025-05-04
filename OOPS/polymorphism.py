
# ===============
# POLYMORPHISM
# ===============

# Polymorphism means "many forms". In python, it allows us to to define different class with the same method name, but the methods can perform different actions according to the context of the classes objects
# Types of Polymorphism

# | **Type**                    | **Description**                                                                           | **Example**                                |
# |-----------------------------|------------------------------------------------------------------------------------------ |--------------------------------------------|
# | **1. Compile-time (Static)**| Achieved using method overloading (not natively supported in Python)                      | Function with default args / `*args`       |
# | **2. Run-time (Dynamic)**   | Achieved via method overriding — child class provides specific implementation of a method | Subclass overrides method from superclass  |
# | **3. Duck Typing**          | Python-specific: behavior depends on method availability, not class inheritance           | "If it quacks like a duck…"                |


# Runtime polymorphism - Dynamic Polymorphism - can achieved by using Method Overriding
# a child class overrides the parent class method on the context of objects

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Runtime polymorphism
def make_sound(animal):
    animal.sound()

make_sound(Dog())  # Bark
make_sound(Cat())  # Meow

# ***Duck Typing*** is a concept where the type or class of an object is less important than the methods it defines or the behavior it exhibits.
# "If it looks like a duck, swims like a duck, and quacks like a duck — then it probably is a duck."
# Python doesn’t care what type an object is — if the object implements the expected methods/attributes, it can be used as needed.

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(entity):
    entity.quack()

make_it_quack(Duck())     
make_it_quack(Person())   

