# # # ######################################################### Practice Problem ############################################################

# # # # 20 questions to master oops fundamentals

# # # #######################################################################################################################################

# # # -------------------------------------------------------------------------------------
# # # -------------------------------------------------------------------------------------

# # Encapsulation and @property (Problems 8-9)

# # 8. Bank Account
# # Create BankAccount with private __account_number and __balance.
# # deposit(amount): raise ValueError if amount <= 0
# # withdraw(amount): raise ValueError if amount is more than the balance
# # a read-only balance property (getter only)
# # Test: deposit, withdraw, try to withdraw too much, try acc.balance = 5 (it should fail).
# # Concepts: private variables, @property, raise
# # Hint: Use raise ValueError("message") for invalid cases. For the property, 
# # write only @property def balance(self): return self.__balance and no setter. Use try/except ValueError when testing.

# class BankAccount:

#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("amount invalid")
#         else:
#             self.__balance = self.__balance + amount

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             raise ValueError("Insuffient balance")
#         else:
#             self.__balance = self.__balance - amount

#     @property
#     def balance(self):
#         return self.__balance

# acc = BankAccount("2131342657123", 3432)
# print(acc.balance)

# acc.deposit(568)
# print(acc.balance)

# acc.withdraw(2000)
# print(acc.balance)

# # acc.deposit(-568)
# # print(acc.balance)

# acc.withdraw(3000)
# print(acc.balance)

        
# # # -------------------------------------------------------------------------------------

# # 9. Student with Validated Marks
# # Create Student with name and private __marks. 
# # Add a marks property with a setter that only accepts values from 0 to 100, otherwise raises ValueError. The constructor should also use the setter.
# # Concepts: getter, setter, validation
# # Hint: Write @property def marks and @marks.setter def marks(self, value). 
# # In __init__, write self.marks = marks (no underscores) so it goes through the setter and gets validated. The setter finally stores self.__marks = value.

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
        



# # # -------------------------------------------------------------------------------------
# # # -------------------------------------------------------------------------------------

# # Inheritance, super(), Overriding (Problems 10-13)
# # 10. Vehicle, Car, Bike
# # Create Vehicle with name and speed, and a method describe(). Create Car (extra: doors) and Bike (extra: has_gear). 
# # Both call super().__init__() and override describe() to include their extra info.
# # Concepts: single inheritance, super().__init__, overriding
# # Hint: In the child __init__, first call super().__init__(name, speed), then set the extra variable.
# #  In the child describe, you can call super().describe() first, then print the extra details.

# # # -------------------------------------------------------------------------------------

# # 11. Animals Speak (polymorphism)
# # Create Animal with name and speak(). Create Dog, Cat, Cow that each override speak(). Put one of each in a list and loop through it calling speak().
# # Concepts: hierarchical inheritance, polymorphism
# # Hint: The loop is only 2 lines: for a in animals: a.speak(). The magic is that the same line gives 3 different outputs.

# # # -------------------------------------------------------------------------------------

# # 12. Person → Employee → Manager (multilevel)
# # Person: name, age
# # Employee(Person): adds salary
# # Manager(Employee): adds a list team, and a method add_member(employee)
# # Print a manager's name, salary, and team size.
# # Concepts: multilevel inheritance, chaining super()
# # Hint: Each __init__ calls super().__init__(...) with the values its parent needs, then sets its own. Create the team list inside Manager.__init__ as self.team = [] (not as a class variable).

# # # -------------------------------------------------------------------------------------

# # 13. Multiple Inheritance and MRO
# # Create Father and Mother, both with a method skills() that prints different text. Create Child(Father, Mother). 
# # Call Child().skills(). Then print Child.mro(). Then swap the order to Child(Mother, Father) and run again.
# # Concepts: multiple inheritance, method resolution order
# # Hint: Python picks the first parent that has the method. The output of mro() shows the exact search order.
# # Notice that swapping the parents changes the result.

# # # -------------------------------------------------------------------------------------
# # # -------------------------------------------------------------------------------------

# # Polymorphism and Abstraction (Problems 14-15)
# # 14. Duck Typing
# # Create Duck, Robot, and Dog, each with a method sound() (no shared parent).
# #  Write a function make_sound(thing) that calls thing.sound(). Call it with all three.
# # Concepts: duck typing
# # Hint: The function does not check the type at all. It only calls thing.sound(). Bonus: pass an object that has no sound() and see the error.

# # # -------------------------------------------------------------------------------------

# # 15. Abstract Shape
# # Create an abstract Shape with abstract methods area() and perimeter(). Implement Circle (radius), Rectangle (length, width), and Triangle (three sides). 
# # Put all in a list, print each one's area and perimeter. Then try Shape() and confirm it fails.
# # Concepts: ABC, @abstractmethodHint: from abc import ABC, abstractmethod. class Shape(ABC):. 
# # In the abstract methods, the body is just pass. For a triangle, perimeter is the sum of 3 sides.
# # Area uses Heron's formula: s = perimeter / 2, then (s*(s-a)*(s-b)*(s-c)) ** 0.5. Use 3.14 for pi.

# # # -------------------------------------------------------------------------------------