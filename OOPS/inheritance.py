
# ==============
# INHERITANCE
# ==============

# Inheritance allows the class (child class or derived class) to inherit the properties and methods from another class (partent class or base class)
# promotes code reusability and extensibility and modular structure and a hierarchical structure.
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Types of Python Inheritance
# Single Inheritance: A child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A class is derived from a class which is also derived from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# Hybrid Inheritance: A combination of more than one type of inheritance.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Dog class inheriting the Animal class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"    # Overrides the speak method

dog = Dog("Arun")
print(dog.speak())

# **Single Inheritence** - One child class can inherit the properties of One Parent Class

# Dog class inherits the properties of the Animal class
# If the child class does not define its own __init__() method, 
# it will automatically inherit the one from the parent class.

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def personInfo(self):
        return f"Employee name: {self.name} || Employee id: {self.id}"

class Employee(Person):
    def info(self):
        return f"Employee name: {self.name} || Employee id: {self.id}"
        
# create object for the child class and access the properties of parent class
employee = Employee("Abinesh", 124576)
print(employee.info())
print(employee.name, employee.id)
# can access the attributes of parent class by object creation

# __init__() function is a constructor method in Python. 
# It initializes the object’s state when the object is created. If the child class does not define its own __init__() method, 
# it will automatically inherit the one from the parent class.

# super() constructor used to call the parent class methods, used with child class __init__ method to initialize inherited attributes
# To reuse code from the parent class.
# Helps with maintainability and avoids repeating initialization code.
# Works well in multiple inheritance scenarios too.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print("Vehicle Constructor Called")
        
    def show_info(self):
        return f"Vehicle Brand: {self.brand}, Vehicle Model: {self.model}"
    
class Car(Vehicle):
    def __init__(self, brand, model, wheels: int, price: int, year: int):
        super().__init__(brand, model) # calls parent class constructor
        self.price = price
        self.wheels = wheels
        self.year = year
        print("Car constructor called")
        
    def car_info(self):
        return f'''
        Car Brand : {self.brand}
        Car Model : {self.model}
        Car wheels: {self.wheels}
        Car price : {self.price}
                '''
toyota = Car("Toyota", "Supra", 4, 2000000, 1994)
print(toyota.show_info())
print(toyota.car_info())

# | Concept              | Role                                                        |
# | `super().__init__()` | Calls the parent class constructor explicitly               |
# | Parent constructor   | Initializes common attributes (`brand`, `model`)            |
# | Child constructor    | Initializes specific attributes (`wheels`, `price`, `year`) |

import random

class Vehicle:
    def __init__(self, brand, wheels: int, engine_number: int):
        self.brand = brand 
        self.wheels = wheels
        self.engine_number = engine_number
        
    def display_vehicle_info(self):
        return {
            "Vehicle Brand"         : self.brand,
            "Vehicle Wheels"        : self.wheels,
            "Vehicle Engine Number" : self.engine_number
        }
        
class Car(Vehicle):
    def __init__(self, brand, wheels: int, engine_number: int, model, price: int, fuel_type):
        super().__init__(brand, wheels, engine_number)
        self.model = model
        self.price = price
        self.fuel_type = fuel_type
    
    def display_car_info(self):
        return {
            "Car Brand"         : self.brand,
            "Car Model"         : self.model,
            "Car Wheels"        : self.wheels,
            "Car Engine Number" : self.engine_number,
            "Car Price"         : self.price,
            "Car Fuel Type"     : self.fuel_type
        }
        
    def car_register(self):
        reg_num = f"{random.randint(100000, 999999):06d}"
        return f"{reg_num}: Your {self.brand} {self.model} Car Registration Successful!"
    
class Bike(Vehicle):
    def __init__(self, brand, model, wheels: int, engine_number: int, type, cc):
        super().__init__(brand, wheels, engine_number)
        self.model = model
        self.cc = cc
        self.type = type
        
    def bike_specs(self):
        return {
            "Bike Brand" : self.brand,
            "Bike Model" : self.model,
            "Bike Wheels": self.wheels,
            "Bike CC"    : self.cc,
            "Bike Type"  : self.type
        }
    
    def bike_register(self):
        reg_num = f"{random.randint(100000, 999999):06d}"
        return f"{reg_num}: Your {self.model} Registration Successful!"
    
# car object creation
car = Car(
    brand="Toyota",
    wheels=4,
    engine_number=14628,
    model="Supra",
    price=1200000,
    fuel_type="Combustion Engine"
)

# access car info and fetch details
car_info = car.display_car_info()

print("Car Details:\n-------------")
for key, value in car_info.items():
    print(f"{key} : {value}")

print(car.car_register())

# bike object creation
bike = Bike(
    brand="Bajaj",
    model="Pulsar N150",
    wheels=2, 
    engine_number=568261,
    type="Sports Cruiser",
    cc=250
)

# access bike info and fetch details
bike_info = bike.bike_specs()

print("\nBike Details:\n-------------")
for key, value in bike_info.items():
    print(f"{key} : {value}")

print(bike.bike_register())

# vehicle object
vehicle = Vehicle(
    brand='Volvo',
    wheels=6,
    engine_number=786462
)

vehicle_info = vehicle.display_vehicle_info()

for key, value in vehicle_info.items():
    print(f"{key} : {value}")


# **Multiple Inheritence** a child class can inherits the properties of more than one parent class, the derived class can inherits al the properties of base class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Work:
    def __init__(self, job_title):
        self.job_title = job_title
    
    def show_job(self):
        print(f"Job : {self.job_title}")

# inherits from both the parents class
class Employee(Person, Work):
    def __init__(self, name, age, job_title, salary):
        # initializes parent class constructor
        Person.__init__(self, name, age)
        Work.__init__(self, job_title)
        self.salary = salary 
        
    def show_details(self):
        print(f'''
        Employee Name   : {self.name}
        Employee Age    : {self.age}
        Employee Job    : {self.job_title}
        Employee Salary : {self.salary}
        ''')
employee = Employee("Abinesh", 23, "Developer", 25000)
employee.show_details()
employee.show_job()
employee.show_name()

print(Employee.__mro__) 

#MRO is the order in which Python searches classes when you call a method or initialize with super() in multiple inheritance.
# Cooperative Initialization is when all classes in a multiple inheritance chain use super(), so each class has
# a chance to initialize its own data safely. Each __init__() calls super().__init__(), and Python moves through the MRO in order.

# | Term                    | Meaning                                                                   |
# |-------------------------|-------------------------------------------------------------------------  |
# | **MRO**                 | Order Python uses to search for methods in multiple inheritance.          |  
# | **super()**             | Calls the next class in the MRO.                                          |
# | **Cooperative Init**    | Every class uses `super()` to allow smooth, conflict-free initialization. |

# | Benefit                              | Why it matters                                                |
# |------------------------------------------------------------------------------------------------------|
# | Allows all classes to be initialized | Even if they don’t know all the arguments upfront             |
# | Enables MRO-safe `super()` chains    | Prevents double initialization and missing arguments          |
# | Makes code cleaner and extensible    | Easy to add new parent classes later without breaking others  |

# Constructor chaining means calling one constructor from another in a multi-class inheritance hierarchy, ensuring that all parent class 
# constructors get called automatically and in the right order.

class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
        print("Person Constructor Called")
    
class Work:
    def __init__(self, job, **kwargs):
        super().__init__(**kwargs)
        self.job = job
        print("Work class Contructor called")

class Employee(Work, Person):
    def __init__(self, name, age, job, salary ):
        super().__init__(name=name, age=age, job=job)
        self.salary = salary
        print("Employee class constructor called")

emp = Employee("Abinesh", 24, "Developer", 22000)

# Excercise
# Smart Device System

# Base: 1
class Device:
    def __init__(self, brand, model, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        self.model = model
    
    def device_info(self):
        print("Device Info: \n" + "-" * 20)
        print(f"Brand    : {self.brand}")
        print(f"Model    : {self.model}")
        
# Base: 2
class Connectivity:
    def __init__(self, bluetooth, wifi_enabled, **kwargs):
        super().__init__(**kwargs)
        self.bluetooth = bluetooth
        self.wifi_enabled = wifi_enabled
        
    def connectivity_info(self):
        print("Connectivity Info: \n" + "-" * 20)
        print(f"Bluetooth:   {self.bluetooth}")
        print(f"WiFi     :   {self.wifi_enabled}")
    
# Child: 1
class SmartPhone(Device, Connectivity):
    def __init__(self, brand, model, bluetooth, wifi_enabled, os, **kwargs):
        super().__init__(brand=brand, 
                         model=model, 
                         bluetooth=bluetooth, 
                         wifi_enabled=wifi_enabled, 
                         **kwargs)
        self.os = os
        
    def phone_info(self):
        print("Smartphone Info: \n" + "-" * 20)
        smartphone = {
            "Brand"      : self.brand,      
            "Model"      : self.model,
            "OS"         : self.os,
            "Bluetooth"  : self.bluetooth,
            "WiFi"       : self.wifi_enabled
        }
        for key, value in smartphone.items():
            print(f"{key:<15} : {value}")  

# Child: 2
class SmartWatch(Device, Connectivity):
    def __init__(self, brand, model, bluetooth, wifi_enabled, heart_rate_monitor, **kwargs):
        super().__init__(brand=brand, 
                         model=model, 
                         bluetooth=bluetooth, 
                         wifi_enabled=wifi_enabled, 
                         **kwargs)
        self.heart_rate_monitor = heart_rate_monitor
    
    def watch_info(self):
        print("Smartwatch Info: \n" + "-" * 20)
        smartwatch = {
            "Brand"              : self.brand,      
            "Model"              : self.model,
            "Heart Rate Monitor" : self.heart_rate_monitor,
            "Bluetooth"          : self.bluetooth,
            "WiFi"               : self.wifi_enabled
        }
        for key, value in smartwatch.items():
            print(f"{key:<20} : {value}")  

# Smart Phone Object
smartphone = SmartPhone(
    brand="Samsung",
    model="Galaxy S22",
    os="Android Pi",
    bluetooth="Yes",
    wifi_enabled="Enabled"
)

smartphone.phone_info()
smartphone.device_info()

# Smart Watch Object
smartwatch = SmartWatch(
    brand="Apple",
    model="Watch Series 9",
    heart_rate_monitor="Yes",
    bluetooth="Yes",
    wifi_enabled="Disabled"
)

smartwatch.watch_info()
smartwatch.device_info()

# ** Multilevel Inheritance ** - Multilevel inheritance means a class is derived from a class that is already derived from another class — forming a chain of inheritance.
#  It allows a class to inherit properties and methods from multiple parent classes, forming a hierarchy similar to a family tree. 


# Base class
class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        
    def show_name(self) -> None:
        print(f"Person Name is:({self.name})")

# Intermediary class - inherits from Base class and also acts as a parent class
class Student(Person):
    def __init__(self, name, stud_id, **kwargs):
        super().__init__(name, **kwargs)
        self.stud_id = stud_id
        
    def show_id(self) -> None:
        print(f"{self.name} student Id is: ({self.stud_id})")
        
# Derived Class - Inherits from both Base and Intermediary class
class GraduateStudent(Student):
    def __init__(self, name, stud_id, degree, **kwargs):
        super().__init__(name, stud_id, **kwargs)
        self.degree = degree
        
    def show_degree(self) -> None:
        print(f"{self.name} has completed ({self.degree}) in 2023")
    
    def run(self):
        self.show_name()
        self.show_id()
        self.show_degree()

# object creation
student = GraduateStudent(
    name="Abinesh",
    stud_id=45686,
    degree="BCA"
)

# student.run()
student.show_name() # From Person Class
student.show_id() # From Student Class
student.show_degree() # From GraduateStudent Class

# Excercise
# Mutiple Inheritance
class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
        
        
    def person_info(self) -> dict:
        display_person: dict = {}
        display_person['name'] = self.name
        display_person['age'] = self.age
        return display_person

class Doctor(Person):
    def __init__(self, name, age, specialization, **kwargs):
        super().__init__(name, age, **kwargs)
        self.specialization = specialization
        
    def doctor_info(self) -> dict:
        # call the parent class method to override them
        display_person: dict = super().person_info()
        display_person['specialization'] = self.specialization
        return display_person

class Surgeon(Doctor):
    def __init__(self, name, age, specialization, surgery_type, **kwargs):
        super().__init__(name, age, specialization, **kwargs)
        self.surgery_type = surgery_type
        
    def display_surgeon_info(self) -> None:
        display_person: dict = super().doctor_info()
        display_person['surgery type'] = self.surgery_type
        for key, value in display_person.items():
            print(f"{key:<20} : {value}")
            
    def show_info(self):
        self.display_surgeon_info()
        
# object creation
doctor = Surgeon(
    name="Abinesh",
    age=24,
    specialization="Orthopedics",
    surgery_type="Bone Replacement"
)

doctor.show_info()
print(doctor.person_info())
print(doctor.doctor_info())
print(doctor.show_info())

# ** Hierarchical Inheritance** - where the multiple child class inherits the properties and attributes of the Same Parent class - promotes code reuability and polymorphism
# each subclass overrides the parent class method
             

class Animal:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        
    def sound(self):
        print(f"This {self.name} makes this sound!")
        
class Dog(Animal):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        
    def sound(self):
        print(f"{self.name} Barks!")
        
class Cat(Animal):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        
    def sound(self):
        print(f"{self.name} meows!")
        
class Lion(Animal):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        
    def sound(self):
        print(f"{self.name} Roars!") 
        
cat = Cat("Snowbell")
cat.sound()       

dog = Dog("Rocky")
dog.sound()

lion = Lion("Simba")
lion.sound()

animal = Animal("Ajay")
animal.sound()

# Excerscise
# School Members

class SchoolMember:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
        
    def get_details(self) -> dict:
        details: dict = {
            "Name": self.name,
            "Age": self.age
        }
        return details


class Student(SchoolMember):
    def __init__(self, name, age, grade, **kwargs):
        super().__init__(name, age, **kwargs)
        self.grade = grade
        
    def get_details(self) -> None:
        details = super().get_details()
        details['Grade'] = self.grade
        print(f"Student Details \n" + "-" * 20)
        for key, value in details.items():
            print(f"{key:<10} : {value}")


class Teacher(SchoolMember):
    def __init__(self, name, age, subject: list, **kwargs):
        super().__init__(name, age, **kwargs)
        self.subject = subject
        
    def get_details(self) -> None:
        details = super().get_details()
        details['Subjects'] = ", ".join(self.subject)  
        print(f"Teacher Details \n" + "-" * 20)
        for key, value in details.items():
            print(f"{key:<10} : {value}")


class Principal(SchoolMember):
    def __init__(self, name, age, experience, **kwargs):
        super().__init__(name, age, **kwargs)
        self.experience = experience
        
    def get_details(self) -> None:
        details = super().get_details()
        details['Experience'] = f"{self.experience} years"
        print(f"Principal Details \n" + "-" * 20)
        for key, value in details.items():
            print(f"{key:<10} : {value}")

student = Student(
    name="Abinesh",
    grade="10th",
    age="17"
)
student.get_details()

teacher = Teacher(
    name="Savitha",
    age="25",
    subject=["Tamil", "English", "Maths"]
)
teacher.get_details()

principal = Principal(
    name="Kamala",
    age="35",
    experience="5"
)
principal.get_details()
                                             
# **Hybrid Inheritance** - Combination of singe, multiple, multilevel inheritance to achieve Hybrid Inheritance - like all the Child class can inherit from parent class and vice versa

# Excercise
# Smart Home System

# Base 1
class Device:
    def __init__(self, brand, model, power_status=False, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        self.model = model
        self.power_status = power_status
        
    def turn_on(self):
        if not self.power_status:
            self.power_status = True
            print(f"{self.brand} {self.model} is now powered ON")
        else:
            print(f"{self.brand} {self.model} is already ON")
    
    def turn_off(self):
        if self.power_status:
            self.power_status = False
            print(f"{self.brand} {self.model} is now powered OFF")
        else:
            print(f"{self.brand} {self.model} is already OFF")

# Base 2
class Connectivity:
    def __init__(self, wifi_enabled, bluetooth_enabled, **kwargs):
        super().__init__(**kwargs)
        self.wifi_enabled = wifi_enabled
        self.bluetooth_enabled = bluetooth_enabled
        
    def connect_wifi(self):
        if not self.wifi_enabled:
            print(f"{self.brand} - {self.model} WiFi not available")
        else:
            print(f"{self.brand} - {self.model} WiFi Connected")
             
    def connect_bluetooth(self):
        if not self.bluetooth_enabled:
            print(f"{self.brand} - {self.model} Bluetooth not available")
        else:
            print(f"{self.brand} - {self.model} Connected via Bluetooth")
            
# Derived 1 - inherit from Base 1 and Base 2
class SmartTV(Device, Connectivity):
    def __init__(self, brand, model, wifi_enabled, bluetooth_enabled, screen_size, resolution, **kwargs):
        super().__init__(brand=brand, model=model, wifi_enabled=wifi_enabled, bluetooth_enabled=bluetooth_enabled, **kwargs)
        self.screen_size = screen_size
        self.resolution = resolution
        
    def stream_app(self, app_name):
        print(f"Streaming {app_name} on {self.brand} SmartTV.")

# Derived 2 - inherit from Base 1 only
class SmartLight(Device):
    def __init__(self, brand, model, power_status, color, brightness, **kwargs):
        super().__init__(brand, model, power_status, **kwargs) 
        self.color = color
        self.brightness = brightness
        
    def change_color(self, color):
        self.color = color
        print(f"Light color changed to {self.color}.")
    
    def dim_light(self, brightness):
        self.brightness = brightness
        print(f"Brightness set to {self.brightness}%.")

# Test SmartTV
tv = SmartTV("Samsung", "QLED-X", True, True, "55 inch", "4K")
tv.turn_on()
tv.connect_wifi()
tv.stream_app("Netflix")

# Test SmartLight
light = SmartLight("Philips", "Hue", False, "White", 100)
light.turn_on()
light.change_color("Blue")
light.dim_light(50)

for cls in SmartTV.__mro__:
    print(cls)
    

# SmartTV: Inherits from both Device and Connectivity → Hybrid Inheritance
# SmartLight: Inherits only from Device → Shows hierarchical structure
# Connectivity & Device have no relation to each other, but are mixed in SmartTV.

# Multiple Inheritance: SmartTV(Device, Connectivity)
# Hierarchical Inheritance: Both SmartTV and SmartLight inherit from Device

# | **Type of Inheritance**      | **Description**                                           | **Example** Structure          | **Use Case / Notes**                                                |
# |------------------------------|-----------------------------------------------------------|--------------------------------|---------------------------------------------------------------------|
# | **Single Inheritance**       | One child class inherits from one parent class            | `Child → Parent`               | Simple reusability of methods/attributes                            |
# | **Multiple Inheritance**     | One child class inherits from multiple parent classes     | `Child → Parent1, Parent2`     | Use `super()` carefully; leads to MRO and potential diamond problem |
# | **Multilevel Inheritance**   | A class inherits from a child class of another class      | `Grandchild → Child → Parent`  | Enables layer-wise specialization                                   |
# | **Hierarchical Inheritance** | Multiple child classes inherit from a single parent class | `Child1, Child2 → Parent`      | Common base logic for different child roles                         |
# | **Hybrid Inheritance**       | Combination of two or more types of inheritance           | Mix of above types             | Often uses `super()` and `**kwargs` to manage complexity            |

# Concept	Meaning	Example / Note
# super()	Calls the next constructor/method in the MRO chain	super().__init__()
# **kwargs in init	Helps pass unused args up the chain — essential for cooperative multiple inheritance	Used in all constructors: def __init__(..., **kwargs)
# Method Resolution Order (MRO)	The order Python follows to search methods in multiple inheritance	ClassName.__mro__ or help(ClassName)
