
######################################################### Magic/Dunder Methods ############################################################

# Dunder = Double UNDERscore. These are special methods with names like __init__ or __str__. You almost never call them yourself. 
# Python calls them automatically when you use certain operations.

# we need it because it let our own objects behave like built-in Python things (printable, comparable, addable, countable).


# Method                Python calls it when you write                   Purpose

# __init__                Student("Rahul")                           Set up a new object
# __str__              print(obj) or str(obj)                        Friendly text for users
# __repr__           typing obj in console, or inside lists          Exact text for developers
# __len__                   len(obj)                                 Return a length
# __eq__                     a == b                                  Define equality
# __lt__                     a < b                                   Define "less than"
# __add__                    a + b                                   Define addition
# __getitem__                obj[0]                                  Allow indexing
# __call__                   obj()                                   Make object callable like a function

# Dunder methods are called by Python. You just define them.

###########################################################################################################################################

# Example: without and with __str__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Rahul", 75)
print(s)         #<__main__.Student object at 0x102fc6660>

# ---------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

s = Student("Rahul", 75)
print(s)          # Student: Rahul, Marks: 75

# ------------------------------------------------------------------------------------

# __str__ vs __repr__

# __str__: for users, readable and friendly.
# __repr__: for developers, precise, ideally shows how to recreate the object.

# If only __repr__ is defined, print() uses it as well. If only __str__ is defined, repr() does not use it.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

s = Student("Rahul", 75)
print(s)            
print(repr(s))      
print([s])          

# Always return a string from __str__ and __repr__ (do not just print inside them).

# ------------------------------------------------------------------------------------


class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        return self.members[index]

t = Team(["a", "b", "b"])
print(len(t))        
print(t[1])         


# ------------------------------------------------------------------------------------


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x

print(Point(1, 2) == Point(1, 2))     
print(Point(1, 2) < Point(5, 0))      

# Without __eq__, Point(1, 2) == Point(1, 2) would be False, because Python compares memory addresses by default.