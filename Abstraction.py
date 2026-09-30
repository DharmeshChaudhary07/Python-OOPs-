
# ######################################################### Abstraction ############################################################

# # Abstraction means showing only the essential idea and hiding the details. In code, we usually create an abstract class: 
# # a class that defines what methods must exist, but leaves how they work to the child classes.
# # ** Abstraction hides complexity, while Encapsulation hides data to ensure safety.**

# # Analogy: A driving licence rule says "every car must have a start() and a stop()". It does not say how each car does it.

# # We need abstraction -> It forces every child class to follow the same structure. If a child forgets a required method, Python raises an error immediately.



# # Syntax -> 

# from abc import ABC, abstractmethod

# class ParentName(ABC):            # inherit from ABC

#     @abstractmethod               # marks the method as required
#     def method_name(self):
#         pass                      # no code here




# # Abstraction   vs   Encapsulation

# # Feature	                   Abstraction                        	Encapsulation

# # Core Intent	             • Hides complexity.                  • Hides data.
# #                            • Shows what it does.                • Restricts direct access.
# #                            • Conceals how it works.	          • Protects internal state.

# # Focus	                     • Focuses on design.                 • Focuses on implementation.
# #                            • Prioritizes outer interface.	      • Prioritizes internal security.

# # How its achieved	         • Uses Abstract Classes.             • Uses Access Modifiers.
# #                            • Uses Interfaces.	                  • Uses Getters and Setters.

# # Real-World Analogy	     • Driving a Car.                     • Medical Capsule.
# #                            • You press the pedal.               • Plastic shell wraps medicine.
# #                            • You ignore engine physics.	      • Shell prevents contamination.


# ###################################################################################################################################

# # Example 1

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class rectangle(shape):

    def __init__(self, len, width):
        self.len = len
        self.width = width

    def area(self):
        return self.len * self.width

c = circle(5)
print(c.area())

r = rectangle(3,5)
print(r.area())

# s = shape()   #  TypeError: Can't instantiate abstract class shape without an implementation for abstract method 'area'
# print(s)

# ----------------------------------------------------------------------------------------

# What happens if a child forgets the method?

# class Triangle(Shape):
#     pass                      # did not write area()

# t = Triangle()                # ERROR: Can't instantiate abstract class Triangle
#                               # with abstract method area

# ----------------------------------------------------------------------------------------
    
# Example 2

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass

    def __str__(self):
        return f"{self.name} earns {self.salary()}"

class FullTime(Employee):
    def __init__(self, name, monthly):
        super().__init__(name)
        self.monthly = monthly

    def salary(self):
        return self.monthly

class Hourly(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate = rate
        self.hours = hours

    def salary(self):
        return self.rate * self.hours

staff = [FullTime("Asha", 50000), Hourly("Ravi", 200, 120)]

for e in staff:
    print(e)


# ----------------------------------------------------------------------------------------
    
# Example 3 (ETL) steps


from abc import ABC, abstractmethod

class ETLStep(ABC):
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def load(self, data):
        pass

    def run(self):                      # same for every step
        data = self.extract()
        data = self.transform(data)
        self.load(data)

class SalesETL(ETLStep):
    def extract(self):
        return [100, 200, 300]

    def transform(self, data):
        return [x * 1.18 for x in data]   # add 18% tax

    def load(self, data):
        print("Loading:", data)

SalesETL().run()