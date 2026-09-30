
######################################################### Practice Problem ############################################################
# Composition (Has-A) vs Inheritance (Is-A)

# Inheritance ("is-a"): a Dog is an Animal.

# Composition ("has-a"): a Car has an Engine. One class contains an object of another class.

#######################################################################################################################################

# The test
# Ask: "Is X a type of Y?"
# Yes: use inheritance.
# No, X just contains or uses Y: use composition.

# Example 

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()       # Car HAS an Engine

    def start(self):
        self.engine.start()
        print("Car is ready to drive")


Car().start()
# Engine started
# Car is ready to drive

# ---------------------------------------------------------------------

# ​Writing class Car(Engine) would be wrong, because a Car is not a type of Engine.

# Why composition is often preferred
# Easier to change (swap the engine without touching the car's family tree).
# Avoids deep, confusing inheritance chains.
# The design rule "favor composition over inheritance" is well known.

# ----------------------------------------------------------------------
# Example: 

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []              # Library HAS books

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            print(b.title)

lib = Library()
lib.add_book(Book("Python Basics"))
lib.add_book(Book("Data Engineering"))
lib.show_books()

#######################################################################################################################################

#  Useful Built-in Functions 

class Animal: 
    pass
class Dog(Animal): 
    pass

d = Dog()

print(isinstance(d, Dog))        # True   (is d an object of Dog?)
print(isinstance(d, Animal))     # True   (Dog is also an Animal)
print(issubclass(Dog, Animal))   # True   (is Dog a child of Animal?)
print(type(d))                   # <class '__main__.Dog'>

# Working with attributes dynamically

class Student:
    def __init__(self, name):
        self.name = name

s = Student("Rahul")
print(hasattr(s, "name"))        # True
print(getattr(s, "name"))        # Rahul
setattr(s, "marks", 90)          # adds s.marks = 90
print(s.marks)                   # 90
print(s.__dict__)                # {'name': 'Rahul', 'marks': 90} 