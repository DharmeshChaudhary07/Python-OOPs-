
################################################## Instance variable vs class variable #################################################

# Instance variable — belongs to one object, set via self.x (usually in __init__). Different for every object.

# Class variable — belongs to the class itself, written directly under the class (not inside any method). Shared by every object unless overridden.

########################################################################################################################################

class Dog:
    species = "Canis familiaris"   # class variable — same for ALL dogs

    def __init__(self, name):
        self.name = name            # instance variable — unique per dog

d1 = Dog("Rex")
d2 = Dog("Milo")

print(d1.species)   # Canis familiaris
print(d2.species)   # Canis familiaris
print(d1.name)       # Rex
print(d2.name)       # Milo

Dog.species = "Updated"   # change it on the class

print(d1.species)          # Updated — affects all instances


################################################## Methods - class, instance and static #################################################

# Instance Method: An Instance Method is a function defined inside a class that operates directly on an individual object (instance) of that class.
# It automatically receives self as its first parameter, which points directly to the specific object calling the method.
# Capability: It has full access to read and modify both the object's unique instance variables and the class's shared variables.
'Instance method: Making a specific pizza for a customer (adds toppings to that specific pizza).'


# Class Method: A Class Method is a function bound to the class itself, rather than any individual object. 
# It is marked with the @classmethod decorator and automatically receives cls as its first parameter, which points to the class blueprint.
# Capability: It can read and modify variables that belong to the class as a whole, affecting all instances simultaneously. 
# It cannot access object-specific instance variables because it doesn't know which individual object is calling it.
'Class method: Changing the name of the whole franchise (affects every shop and pizza).'


# static Method: A Static Method is a standard utility function that is logically grouped inside a class but remains completely isolated from the class and 
# its instances. It is marked with the @staticmethod decorator and does not receive self or cls as an automatic first parameter.
# Capability: It acts like a regular independent function. It cannot read or modify either the object's instance variables or the class's variables.
'Static Method: Checking if the weather is good for delivery (doesnt change the pizza or the shop name, its just helpful info).'

########################################################################################################################################

# Example 1

class PizzaShop:
    
    shop_name = "Mario's Pizza"         # Class Variable (Shared by everyone)

    def __init__(self, topping):
        self.topping = topping          # Instance Variable (Unique to this one pizza)

    # 1. Instance Method (Uses 'self' to look at your specific pizza)
    def describe_pizza(self):
        print(f"This is a {self.topping} pizza from {self.shop_name}.")


    # 2. Class Method (Uses 'cls' to change the whole shop)
    @classmethod
    def rename_shop(cls, new_name):
        cls.shop_name = new_name


    # 3. Static Method (Just a regular helper function, uses no self or cls)
    @staticmethod
    def is_pizza_healthy(topping):
        if topping == "Salad":
            return True
        return False


# Make two different pizzas
my_pizza = PizzaShop("Pepperoni")
your_pizza = PizzaShop("Cheese")


my_pizza.describe_pizza()  # instance method  # prints ->  This is a Pepperoni pizza from Mario's Pizza.


PizzaShop.rename_shop("Mega Pizza")
your_pizza.describe_pizza()  # class method # prints -> This is a Cheese pizza from Mega Pizza.


print(PizzaShop.is_pizza_healthy("Salad"))  # static method # prints -> False

--------------------------------------------------------------------------

# Example 2

class carfactory:
    total_car_build = 0          # class variable

    def __init__(self, model):  
        self.model = model      # instance variable 
        self.fuel = 525         # instance variable 

        carfactory.total_car_build = carfactory.total_car_build + 1

    def drive(self, distance):
        self.fuel = self.fuel - distance * 2.4
        print(f'I am driving {self.model}, fuel left: {self.fuel}')

    @classmethod
    def get_report(cls):
        print(f'total no of car build is {cls.total_car_build}')

    @staticmethod
    def convert_mph_to_kph(mph):
        return mph * 1.609


car = carfactory('audi')

car.drive(94)    # instance 

carfactory.get_report()
        
speed_kph = carfactory.convert_mph_to_kph(90)
print(f'speed in kph is: {speed_kph}' )