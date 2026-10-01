# # ######################################################### Practice Problem ############################################################

# # # 20 questions to master oops fundamentals

# # #######################################################################################################################################

# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------

# Encapsulation and @property (Problems 8-9)

# 8. Bank Account
# Create BankAccount with private __account_number and __balance.
# deposit(amount): raise ValueError if amount <= 0
# withdraw(amount): raise ValueError if amount is more than the balance
# a read-only balance property (getter only)
# Test: deposit, withdraw, try to withdraw too much, try acc.balance = 5 (it should fail).
# Concepts: private variables, @property, raise
# Hint: Use raise ValueError("message") for invalid cases. For the property, 
# write only @property def balance(self): return self.__balance and no setter. Use try/except ValueError when testing.

class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount invalid")
        else:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insuffient balance")
        else:
            self.__balance = self.__balance - amount

    @property
    def balance(self):
        return self.__balance

acc = BankAccount("2131342657123", 3432)
print(acc.balance)

acc.deposit(568)
print(acc.balance)

acc.withdraw(2000)
print(acc.balance)

# acc.deposit(-568)
# print(acc.balance)

acc.withdraw(3000)
print(acc.balance)

        
# # -------------------------------------------------------------------------------------

# 9. Student with Validated Marks
# Create Student with name and private __marks. 
# Add a marks property with a setter that only accepts values from 0 to 100, otherwise raises ValueError. The constructor should also use the setter.
# Concepts: getter, setter, validation
# Hint: Write @property def marks and @marks.setter def marks(self, value). 
# In __init__, write self.marks = marks (no underscores) so it goes through the setter and gets validated. The setter finally stores self.__marks = value.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0  or value > 100:
            # print("invalid")
            raise ValueError("marks no valid")
        else:
            self.__marks = value

stud = Student("Kiara", 90)
print(stud.marks)
stud2 = Student("coby", 122)
print(stud2.marks)
stud2.marks = 300
print(stud2.marks)
        



# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------

# Inheritance, super(), Overriding (Problems 10-13)
# 10. Vehicle, Car, Bike
# Create Vehicle with name and speed, and a method describe(). Create Car (extra: doors) and Bike (extra: has_gear). 
# Both call super().__init__() and override describe() to include their extra info.
# Concepts: single inheritance, super().__init__, overriding
# Hint: In the child __init__, first call super().__init__(name, speed), then set the extra variable.
#  In the child describe, you can call super().describe() first, then print the extra details.

class Vehicle:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed 

    def describe(self):
        print(f"its a {self.name} and its top speed is {self.speed}")
    

class Car(Vehicle):

    def __init__(self, name, speed, door):
        super().__init__(name , speed )
        self.door = door

    def describe(self):
        super().describe()
        print(f"the car has {self.door} door")


class Bike(Vehicle):

    def __init__(self, name, speed, has_gear):
        super().__init__(name , speed)
        self.has_gear = has_gear

    def describe(self):
        super().describe()
        print(f"it has {self.has_gear}")
              
car = Car("Audi", 260, 4)
car.describe()
bike = Bike("Redbull", 345, 8)
bike.describe()
    



# # -------------------------------------------------------------------------------------

# 11. Animals Speak (polymorphism)
# Create Animal with name and speak(). Create Dog, Cat, Cow that each override speak(). Put one of each in a list and loop through it calling speak().
# Concepts: hierarchical inheritance, polymorphism
# Hint: The loop is only 2 lines: for a in animals: a.speak(). The magic is that the same line gives 3 different outputs.

class Animal:
    def __init__(self, name):
        self.name = name 

    def speaK(self):
        print(f"{self.name} make sound)")

class Dog(Animal):
    def speaK(self):
        print(f"{self.name} says Woof")
    
class Cat(Animal):
    def speaK(self):
        print(f"{self.name} says Meow")

class Cow(Animal):
    def speaK(self):
        print(f"{self.name} says Mooh")

animal = [Dog("alex"), Cat("kitty"), Cow("Radha")]

for i in animal:
    i.speaK()



# # -------------------------------------------------------------------------------------

# 12. Person → Employee → Manager (multilevel)
# Person: name, age
# Employee(Person): adds salary
# Manager(Employee): adds a list team, and a method add_member(employee)
# Print a manager's name, salary, and team size.
# Concepts: multilevel inheritance, chaining super()
# Hint: Each __init__ calls super().__init__(...) with the values its parent needs, then sets its own. 
# Create the team list inside Manager.__init__ as self.team = [] (not as a class variable).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person): 
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.team = []

    def add_member(self, member):
        self.team.append(member)

m = Manager("kiara",24, 89000)

e1 = Employee("Ahana", 23, 83000)
e2 = Employee("Aung", 25, 64000)

m.add_member(e1)
m.add_member(e2)

print(m.name, m.salary, len(m.team))


# # -------------------------------------------------------------------------------------

# 13. Multiple Inheritance and MRO
# Create Father and Mother, both with a method skills() that prints different text. Create Child(Father, Mother). 
# Call Child().skills(). Then print Child.mro(). Then swap the order to Child(Mother, Father) and run again.
# Concepts: multiple inheritance, method resolution order
# Hint: Python picks the first parent that has the method. The output of mro() shows the exact search order.
# Notice that swapping the parents changes the result.

class Father:
    def skills(self):
        print("a")

class Mother:
    def skills(self):
        print("b")

class Child(Father, Mother):
    pass

Child().skills()
print(Child.mro())

class Father:
    def skills(self):
        print("a")

class Mother:
    def skills(self):
        print("b")

class Child(Mother, Father):
    pass

Child().skills()
print(Child.mro())

# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------

# Polymorphism and Abstraction (Problems 14-15)

# 14. Duck Typing
# Create Duck, Robot, and Dog, each with a method sound() (no shared parent).
#  Write a function make_sound(thing) that calls thing.sound(). Call it with all three.
# Concepts: duck typing
# Hint: The function does not check the type at all. It only calls thing.sound(). Bonus: pass an object that has no sound() and see the error.

class Duck:
    def sound(self):
        print("duck sound quack")

class Robot:
    def sound(self):
        print("robot sounds krrkrkrkrkrk")

class Dog:
    def sound(self):
        print("dog sounds woof")

def make_sound(thing):
    thing.sound()

make_sound(Duck())
make_sound(Robot())
make_sound(Dog())


# # -------------------------------------------------------------------------------------

# 15. Abstract Shape
# Create an abstract Shape with abstract methods area() and perimeter(). Implement Circle (radius), Rectangle (length, width), and Triangle (three sides). 
# Put all in a list, print each one's area and perimeter. Then try Shape() and confirm it fails.
# Concepts: ABC, @abstractmethodHint: from abc import ABC, abstractmethod. class Shape(ABC):. 
# In the abstract methods, the body is just pass. For a triangle, perimeter is the sum of 3 sides.
# Area uses Heron's formula: s = perimeter / 2, then (s*(s-a)*(s-b)*(s-c)) ** 0.5. Use 3.14 for pi.

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

class Triangle(Shape):

    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def area(self):
        s = (self.l + self.b + self.h)/ 2
        return (s * (s - self.l) * (s - self.b) * (s-self.h)) ** 0.5


    def perimeter(self):
        return self.l + self.b + self.h
    

c = Circle(63)
print(c.area())
print(round(c.perimeter(),2))

r = Rectangle(25,45)
print(r.area())
print(r.perimeter())

t = Triangle(63,45,57)
print(round(t.area(),2))
print(t.perimeter())


# # -------------------------------------------------------------------------------------