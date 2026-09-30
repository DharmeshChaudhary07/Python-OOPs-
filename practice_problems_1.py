
######################################################### Practice Problem ############################################################

# 20 questions to master oops fundamentals

#######################################################################################################################################

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

# Class, __init__,(Problems 1-3)

# 1. Rectangle

# Create a Rectangle class with length and width. Add methods area() and perimeter() that return the values. 
# Create two rectangles and print their area and perimeter.
# Concepts: class, __init__, self, instance methods

class rectangle:

    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width) 

shape = rectangle(10,20)
print(shape.area())
print(shape.perimeter())

# -------------------------------------------------------------------------------------

# 2. Book

# Create a Book class with title, author, price. Add show() that prints all details on one line. 
# Add apply_discount(percent) that reduces the price. Create 3 books and apply a discount on one.
# Concepts: methods that change object data

class book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        return (f"i am reading a book title {self.title}, written by {self.author},  purchased for {self.price}")
    
    def apply_discount(self, percent):
        self.percent = percent
        self.price = self.price - (self.percent * self.price / 100)

reading = book("abc", "ashoe", 200)
# reading.show()
print(reading.show()) 
reading.apply_discount(50)
print(reading.show()) 


# reading.show() -> Use it when the show() method itself contains print().
# print(reading.show()) -> Use it when the show() method uses return, not print().

# -------------------------------------------------------------------------------------

# 3. Student

# Create a Student with name and marks. Add get_grade() that returns "A" if marks >= 80, "B" if >= 60, "C" if >= 40, else "Fail".
# Concepts: if/elif/else inside a method

class student:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_grade(self):
        if self.mark >= 80:
            return "A"
        elif self.mark >= 60:
            return "B"
        elif self.mark >= 40:
            return "C"
        else:
            return "Fail"

stud = student("Alex", 39)
print(stud.get_grade())
    


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

# Instance vs Class Variables, and the 3 Method Types (Problems 4-7)

# 4. Object Counter
# Create a Counter class with a class variable count = 0. Every time a new object is created, count increases by 1.
# Create 5 objects and print Counter.count.
# Concepts: class variable, changing it from __init__


class counter:

    variable_count = 0

    def __init__(self):
        counter.variable_count += 1

        

var = counter()
print(counter.variable_count)
var2 = counter()
print(counter.variable_count)
var3 = counter()
print(counter.variable_count)
var4 = counter()
print(counter.variable_count)
var5 = counter()
print(counter.variable_count)

print(counter.self.count)



# -------------------------------------------------------------------------------------

# 5. Employee with Company Name

# Create Employee with a class variable company_name = "TechCorp" and instance variables name and salary.
#  Add a @classmethod change_company(cls, new_name). Create 3 employees, change the company, and print company_name from each employee.
# Concepts: class variable, @classmethod

class employerr:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary

    def emply(self):
        print(f'{self.name}, {self.salary} working at {self.company_name}' )

    @classmethod 
    def change_company(cls, new_name):
        cls.company_name = new_name
        

emp1 = employerr("alex", 40000)
# print(emp1)
emp1.emply()
emp2 = employerr("kiara", 82000)
emp2.emply()
emp3 = employerr("saina", 40000)
emp3.emply()

employerr.change_company("POK")
emp1.emply()
emp2.emply()
emp3.emply()


# -------------------------------------------------------------------------------------

# 6. Alternate Constructor and Static Validator

# In Employee (from problem 5), add:
# @classmethod from_string(cls, text) that takes "Rahul-50000" and returns an Employee
# @staticmethod is_valid_salary(amount) that returns True if the amount is greater than 0
# Create an employee using Employee.from_string("Rahul-50000").
# Concepts: @classmethod as constructor, @staticmethod

Hint: Use text.split("-") to get name and salary. Convert salary with int(). The class method ends with return cls(name, salary).
 The static method has no self and no cls.


class employerr:

    def __init__(self, name, salary):
        if not employerr.is_valid_salary(salary):
            raise ValueError("Not a valid salary")
        self.name= name
        self.salary = salary

    def emply(self):
        print(f'{self.name}, {self.salary}' )

    @classmethod
    def from_string(cls, text):
        name ,salary = text.split("-") 
        return cls(name, int(salary))
    
    @staticmethod 
    def is_valid_salary(amount):
        if amount > 0:
            return True
        return False
    
emp = employerr.from_string("Rahul-50000")
print(emp.name , emp.salary)
emp.emply()

# print(employerr.is_valid_salary(50000))   # True
# print(employerr.is_valid_salary(-500))     # False

# emp2 = employerr.from_string("Priya--5000")   # this should raise ValueError

emp4 = employerr("Priya", -5000)   # this should raise ValueError: Not a valid salary


# -------------------------------------------------------------------------------------


# 7. ATM Rewrite (your own code, done properly)
# Rewrite your ATM program with:
# a class variable bank_name
# private __pin and __balance
# a @staticmethod is_valid_pin(pin) that checks the pin is exactly 4 digits
# create_pin, deposit, withdraw, check_balance (keep your menu loop if you like).  
# Concepts: private variables, static method, class variable


class atm:
    bank_name = "hdfc"

    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    @staticmethod
    def is_valid_pin(pin):
        if len(pin) == 4 and pin.isdigit():
            return "pin is valid"
        return "pin not valid"

    def change_pin(self, old_pin, new_pin):

        if old_pin != self.__pin:
            return "Incorrect current pin"
        
        if not atm.is_valid_pin(new_pin):
            return "New pin must be exactly 4 digits"
        self.__pin = new_pin
        return "Pin changed successfully"

money = atm.is_valid_pin("1233")
print(money)
money1 = atm.is_valid_pin("66798")
print(money1)

acc = atm("1233", 5000)
print(acc.change_pin("1233", "55778"))  # New pin must be exactly 4 digits
print(acc.change_pin("1233", "5577"))   # Pin changed successfully


