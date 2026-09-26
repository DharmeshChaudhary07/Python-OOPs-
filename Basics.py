
#############################################   Object Oriented Programming  ##########################################################

'''

Class -> A class is a blueprint for creating objects.
It defines a set of attributes and methods that the created objects will have

        example: class Car:  

        (colr, model, year) -> attributes
        def start_engine(self):  -> method




Object -> An object is an instance of a class. It is created based on the blueprint defined by the class and can have its own unique 
values for the attributes defined in the class.

    example: my_car = Car(),


########################################


Function vs Method -> 

A function is a block of code that performs a specific task and can be called independently. 

A method, on the other hand, is a function that is defined within a class and is associated with an object of that class. 
Methods can access and modify the attributes of the object they belong to.


########################################


 Always declare variables inside the class and outside the methods, so that they can be accessed by all the methods of the class.



Constructor -> A constructor is a special method in a class that is automatically called when an object of the class is created.
It is used to initialize the attributes of the object with specific values. In Python, the constructor is defined using the __init__ method.

__init__ method -> The __init__ method is a special method in Python classes that is automatically called when an object of the class is created.
It is used to initialize the attributes of the object with specific values.

Syntax: class car:

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

# self refers to the specific object being created.
# color, model, year are just local parameter names — temporary values passed in when you create the object.
# self.color = color means: "store this color value onto the object itself" so it can be accessed later through that object, even after __init__ finishes running.

self is a reference to the current instance of the class. It allows you to access the attributes and methods of the object being created or manipulated.

'''

#################################################################################################################################


class Car:
    def __init__(self):
        print("Hello, I am a constructor")

    def menu(self):
        print("1. Start Engine")
        print("1. Stop Engine")



car1 = Car()    # here car()-> is a class and car1 is an object of the class car 

# Car() — calling it with parentheses creates a brand new object (this is called instantiation). 
# This automatically triggers __init__, which runs and sets up that object's own data (in your example, just prints the message; in 
# your earlier color/model/year example, it would store those values onto this specific object).



car1.menu()

# this calls the menu method, and Python automatically knows to run it on car1 specifically (that's what self refers to inside the method). 
# If you had car2 = Car() as well, car2.menu() would run independently on car2's own data, not car1's.

###############################################


class atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0

    def func(self):

        user_input = input(''' Enter your choice:
                            1. Create Pin
                            2. Check Balance
                            3. Deposit
                            4. Withdraw
                            5. Exit          
                        ''')
        if user_input == '1':
            print("Create Pin")
        elif user_input == '2':
            print("Check Balance")
        elif user_input == '3':
            print("Deposit")
        elif user_input == '4':
            print("Withdraw")
        elif user_input == '5':
            print("Exit")
        else:
            print("Invalid Input")

rich = atm()
rich.func()

###############################################