

# ########################################################## Inheritance ############################################################

# Inheritance lets a new class (child / subclass) automatically get all the variables and methods of an existing class (parent / superclass), 
# and then add or change things.
# Private thing cannot be inherited into child class.

# Example -> A child inherits features from parents but can also have their own.

# use of inheritance 
# 1. reusability of code (login in udemy are same for both(student and instructor) but feature inside are different or student and instructor)


# syntax ->

class Parent:
    pass

class Child(Parent):      # put the parent's name in brackets
    pass

# ###################################################################################################################################

# Example 1

class user:

    def login(self):
        print("login")

    def register(self):
        print("register")

class student(user):

    def course_purchase(self):
        print("purschased")

    def review(self):
        print("reviewed")

hujre = student()   # called class student 
hujre.login()       # called class student but still fetching method from parent class user
hujre.register()
hujre.course_purchase()
hujre.review()

# --------------------------------------------------------------------------------------------------------

# Example 2

class animal:

    def __init__(self, name):
        self.name = name 
        print(f"i am {self.name}")

    def eat(self):
        print(f"{self.name} is eating")

class bark(animal):

    def barking(self):
        print(f"{self.name} is woofing")

dog = bark("reo") 

dog.eat()
dog.barking()

# ###################################################################################################################################

# Method overriding

# A child can replace a parent's method by writing a method with the same name
# method overriding is a type of (runtime) polymorphism, achieved through inheritance.

# ------------------

# Example 1

class animal:
    def sound(self):
        print("some sound")

class dog(animal):
    def eat(self):
        print("i am noob")
    # def sound(self):     
    #     print("dog sound woof")

class cat(animal):
    def sound(self):
        print("cat sounds meow")

animal().sound()
dog().sound()
cat().sound()

# When you call dog().sound(), Python looks for sound in the dog class first. It finds one there, so it runs that and never looks at animal's version.
# That is overriding.
# if there is no method sound in the class dog then i will look upto parent class and fetch from there.

# --------------------------------------------------------------------------------------------------------

# Example 2 

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Paying {self.amount}")

class CreditCard(Payment):
    def pay(self):
        fee = self.amount * 0.02
        print(f"Charging card: {self.amount + fee} (includes 2% fee)")

class UPI(Payment):
    def pay(self):
        print(f"Paid {self.amount} via UPI, no fee")

class CashOnDelivery(Payment):
    def pay(self):
        print(f"Collect {self.amount} in cash at delivery")

orders = [CreditCard(1000), UPI(500), CashOnDelivery(750)]

for order in orders:
    order.pay()      # same call, different behavior

# -----------

# list can hold objects of different classes, and you can loop over it and call the same method on each one.
orders = [CreditCard(1000), UPI(500), CashOnDelivery(750)]
for order in orders:
    order.pay()

# ###################################################################################################################################


# super() is a built-in function that lets a child class call a method from its parent class.

# Its two common uses:
# 1. In __init__: run the parent's setup code, then add the child's own attributes.
# 2. In overridden methods: reuse the parent's version and extend it, instead of replacing it completely.

# Important: If a child defines its own __init__ and forgets super().__init__(...), the parent's __init__ does NOT run, and the parent's variables will be missing.

# ---------------

# Example 1 (in __init__ )'

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)       # parent handles 'name'
        self.breed = breed           # child handles 'breed'

d = Dog("Rex", "Labrador")
print(d.name, d.breed)    # Rex Labrador

# flow is Dog("Rex", "Labrador") -> Dog.__init__(name="Rex") -> super().__init__(name) -> Animal.__init__(name="Rex") -> self.name = "Rex"

# --------------------------------------------------------------------------------------------------------

# Example 2 (overridden methods)

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()                # runs parent's version first
        print("Dog barks")

animal = Dog()
print(animal.speak())

Dog().speak()
# Animal makes a sound
# Dog barks

# ###################################################################################################################################

# Type of Inheritance:
# ------------------------

# 1. Single: one parent, one child

class A: 
    pass
class B(A):
    pass

# ------------------------


# 2. Multilevel: a chain (grandparent, parent, child)

class A:
    pass
class B(A):
    pass
class C(B): 
    pass       # C gets from B, and B got from A

# ------------------------

# 3. Hierarchical: one parent, many children

class Animal: 
    pass
class Dog(Animal): 
    pass
class Cat(Animal): 
    pass

# ------------------------

# 4. Multiple: one child, many parents

class Father:
    def skills(self): 
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

Child().skills()     # Gardening  (Father is listed first, so it wins)

# ------------------------

# 5. Hybrid: a mix of the above (for example, multiple + hierarchical together).

# MRO (Method Resolution Order)
# When several parents have the same method name, Python searches in a fixed order. You can see it:

class A:
    def show(self): 
        print("A")

class B(A):
    def show(self): 
        print("B")

class C(A):
    def show(self): 
        print("C")

class D(C, B):

    pass

D().show()          # B
print(D.mro())      # [D, B, C, A, object]

# mro() is a function its a method that every class has. D.mro() just returns the lookup order as a list: