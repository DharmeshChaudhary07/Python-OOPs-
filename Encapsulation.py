

####################################################### Encapsulations ############################################################

# Encapsulation means two things:

# 1. Bundling data and the methods that use it together in one class.
# 2. Hiding the internal data so it cannot be changed directly from outside. Access happens only through methods you control.

# Example -> An ATM. You cannot reach inside and change the cash count. You can only use the buttons (deposit, withdraw) and 
#            the machine checks the rules before doing anything.


###################################################################################################################################

# why we need -> if we dont hide it anyone can access and modify data.

class atm:
    def __init__(self):
        self.balance = 4000

    def check_from_inside(self):
        print(f"self.balance is: {self.balance}")

account = atm()

account.balance = 9000
account.check_from_inside()


account.balance = 'asdasdas'
account.check_from_inside()


# --------------------------------------------------------------------------------------------------------

# Access levels in Python
# Python has no strict "private" keyword like Java. It uses naming rules:

# Name style                                       Meaning                                      Enforced?

# balance                                   Public, Anyone can use it                              n/a

# _balance                            Protected. "Please don't touch from outside"          No, only a convention
#                                               (a polite hint)

# __balance                           Private. Python renames it internally,                    Mostly yes
#                                             so direct access fails

# --------------------------------------------------------------------------------------------------------

class atm:
    def __init__(self):
        self.__balance = 4000

    def check_from_inside(self):
        print(f"self.balance is: {self.__balance}")

account = atm()
print(account._atm__balance)

account.__balance = 9000
account.check_from_inside()


account.__balance = 'asdasdas'
account.check_from_inside()

account._atm__balance = 5000
account.check_from_inside()

# it doesnot let you change/modify account self.__balance.
# what python does it here is it change/rename the __balance to _atm__balance.
# even after using __ is cannot be kept completely private.

# --------------------------------------------------------------------------------------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Hidden private variable

    # 1. Normal function to READ the balance
    def get_balance(self):
        return self.__balance

    # 2. Normal function to CHANGE the balance safely
    def set_balance(self, value):
        if value < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = value

acc = BankAccount(6000)

# Reading requires brackets because it's a normal function!
print(acc.get_balance())  # Prints: 6000

# Changing requires brackets and passing a value inside!
acc.set_balance(2000)
print(acc.get_balance())  # Prints: 2000

# Testing the safety check
acc.set_balance(-5)       # Prints: Error: Balance cannot be negative!

# --------------------------------------------------------------------------------------------------------

# using the property 

# The Pythonic way: @property
# Writing get_balance() works, but Python has a cleaner way. 
# @property lets you call a method without brackets, like it was a normal variable, while still running your code behind the scenes.

class atm:
    def __init__(self):
        self.__balance = 4000  # 1. The hidden, private variable

    @property
    def balance(self):
        """GETTER: This runs automatically when you type `account.balance`"""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """SETTER: This runs automatically when you type `account.balance = value`"""
        if isinstance(value, str):
            print("Error: You cannot set the balance to text!")
        elif value < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = value


account = atm()

# 1. Reading the balance (No brackets needed!)
# Python secretly redirects this to the @property def balance(self) function
print(account.balance)       # Prints: 4000

# 2. Trying to change it to a string
# Python secretly redirects this to the @balance.setter function
account.balance = 'asdasdas' # Prints: Error: You cannot set the balance to text!
print(account.balance)       # Still prints: 4000 (Safe!)

# 3. Changing it to a valid number
account.balance = 9000       # The setter accepts it silently
print(account.balance)       # Prints: 9000


# --------------------------------------------------------------------------------------------------------

# if we only write getter and not the setter than the value can be read but no be changed.

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2

c = Circle(5)
print(c.area)      # 78.5
c.area = 100       # AttributeError: can't set attribute
# AttributeError: property 'area' of 'Circle' object has no setter


        # @property
        # def area(self):                 # 🟢 GETTER (Has @property)
        #     return 3.14 * self.__radius ** 2

        # @area.setter
        # def area(self, value):          # 🔴 SETTER (Has .setter)
        #     # Python forces you to include a 'value' argument here
        #     print("This is the setter running!") 
