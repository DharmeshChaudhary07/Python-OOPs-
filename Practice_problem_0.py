# # ######################################################### Practice Problem first ############################################################

# # # Practice Questions

# # #######################################################################################################################################

# # -------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------


# 1. Temperature Converter
# Build Temperature with celsius. Add methods to_fahrenheit() and to_kelvin() that return the converted values (don't store them). 
# Create one object, call both methods, and trace what happens from object creation to both method calls finishing.
# Concepts: __init__, return values, basic math

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return self.celsius * 9/5

#     def to_kelvin(self):
#         return self.celsius + 273.15

# temp = Temperature(57)
# print(temp.to_fahrenheit())
# print(temp.to_kelvin())

# # -------------------------------------------------------------------------------------


# 2. Inventory Item with Validation
# Build Item with private __quantity. Add a quantity property (getter + Call describe() on each setter) where the setter rejects negative numbers.
#  Add sell(amount) that reduces quantity, but raises ValueError if amount > quantity. Create one item, sell some stock successfully, 



# class Item:
#     def __init__(self, quantity):
#         self.__quantity = quantity

#     @property
#     def quantity(self):
#         return self.__quantity

#     @quantity.setter
#     def quantity(self, value):
#         if value < 0:
#             print("incorrect item quantity")
#         self.__quantity = value

# product = Item(45)
# print(product.quantity)

# product.quantity = 43
# print(product.quantity)


# # -------------------------------------------------------------------------------------


# 3. Shape Hierarchy with a Shared Method
# Build abstract Shape with abstract area(), and a normal (non-abstract) method describe() that prints f"This shape has an area of {self.area()}". 
# Build Circle and Square. — note that describe() itself never changes, but it calls self.area(), 
# which is different for each child. Trace through one describe() call for Circle, step by step, showing exactly when area() gets called and by what.
# Concepts: abstraction + polymorphism working together
# Hint: This is the real "aha" moment of polymorphism — a method defined ONCE in the parent (describe) automatically behaves differently per child, 
# because of the line self.area() inside it.

# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass
    
#     def describe(self):
#         print (f'This shape has an area of {self.area()}')

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):

#     def __init__(self, a):
#         self.a = a

#     def area(self):
#         return self.a ** 2

# area = Circle(6)
# area.describe()

# area = Square(8)
# area.describe()

# # -------------------------------------------------------------------------------------

# 4. A Class That Calls Its Own Methods
# Build Order with a list of items (each item is (name, price)). 
# Add: add_item(name, price)
# total() that returns the sum of all prices
# summary() that calls self.total() internally and prints f"Total: {total}"
# Trace what happens inside summary() — specifically, how it reaches into total().
# Concepts: one method calling another method on the same object
# Hint: Inside summary, you must write self.total(), not just total(). 
# This is the single most common error across all your submissions so far — a method needs self. to call a sibling method.


class Orders:

    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))
         
    def total(self):
        total_price = 0 
        for name, price in self.items:
            total_price += price
        return total_price

    def summary(self):
        t = self.total()
        print (f"total: {t}")
         
s = Orders()
s.add_item("sushi", 2790)
s.add_item("Pizza", 630)
s.summary()




# # -------------------------------------------------------------------------------------


# 5. Mini System: Students and a Classroom
# Build Student (name, private __marks, property with validation 0-100). Build Classroom that has a list of Student objects (composition), with:
# add_student(student)
# average_marks() — loops through students, returns the average
# topper() — returns the student object with the highest marks
# Create a classroom with 3 students, call both methods, and trace through topper() specifically: how does it compare students, what does it return, and how do you then print the topper's name from outside?
# Concepts: composition, properties, loops over objects, returning an object (not just a number)
# Hint: For topper(), loop through self.students, keep track of the "best so far" student object (not just their marks), and return that student object at the end. Outside, you'd then do classroom.topper().name.

# # -------------------------------------------------------------------------------------
