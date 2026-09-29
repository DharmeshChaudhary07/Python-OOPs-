
######################################################### Polymorphism ############################################################

# Polymorphism means "many forms". It allows functions or methods with the same name to work differently depending on the type of object they are acting upon.
# Polymorphism means "same operation, different behavior." 

# Analogy: The word "play" means different things for a guitarist, a footballer, and an actor.

# Why we need polymorphism -> You can write one piece of code that works with many different types of objects, without checking what type each one is.
# (In oops , Inheritance is what creates the family relationship between classes, but Polymorphism is the actual mechanism that 
# lets your code treat different child objects as if they were the parent type, without checking their specific identity.)



# Different types of polymorphism, showing how a single interface can exhibit multiple behaviors at compile-time and run-time.

# Compile time polymorphism -> 1. Method overloading 
# Runtime polymorphism -> 2. Method overriding 
#                         3. Duck typing
#                         4. Operator overloading 
###################################################################################################################################

 
# Runtime polymorphism 
# 1. Method overriding

class cat:
    def sound(self):
        print("sounds like meow")

class dog:
    def sound(self):
        print("sounds like woof")

class cow:
    def sound(self):
        print("sounds like mooh")

animal = [cat(), dog(), cow()]

for i in animal:
    i.sound()                   # same method differnet behaviour


# ------------------------------------------------------

# 2. Duck typing 

# Python does not care what class an object belongs to. It only cares whether the object has the method you are calling. 
# The saying is: "If it walks like a duck and quacks like a duck, it is a duck."

class duck:
    def sound(self):
        print("quack")

class robot:
    def sound(self):
        print("qrqrqrqrqrq")

def make_sound(speak):
    speak.sound()

# Duck typing allows an outside function to access any object's method as long as that method exists inside the object's class.

make_sound(duck())
make_sound(robot())

# ------------------------------------------------------

# ****
# Method overloading (Python is different from Java here).

# In Java you can have many methods with the same name and different parameters. Python does not support this. 
# If you write the same name twice, the last one replaces the first:

class calc:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calculation = calc()
print(calculation.add(1,2))             # TypeError: calc.add() missing 1 required positional argument: 'c'
                                        # the latest method replace the first method 

# for these kind of problem we can use default argument or *args

class calc:
    def add(self, *num):
        return sum(num)
    
calculation = calc()
print(calculation.add(1,2,3,4,5))

# --------------------------------------------------------------------------------------------------------------

# Compile time polymorphism -> 1. Method overloading 
# Normally + only works on built-in types like numbers and strings. If you try p1 + p2 on a plain class, Python raises a TypeError because it doesnt 
# know what to add point in a plain Operator overloading lets you define that meaning yourself.

class plain_point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return plain_point(self.x + other.x , self.y + other.y)

    def __str__(self):
        return "{},{}".format(self.x , self.y)
        # return f"{self.x , self.y}"

p1 = plain_point(1,2)
p2 = plain_point(2,4)
print(p1 + p2)

# --------------------------------------------------------------------------------------------------------------
