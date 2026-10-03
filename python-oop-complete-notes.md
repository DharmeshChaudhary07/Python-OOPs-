# Python OOP: Complete Notes in Simple Language

**How to use these notes:** Read one section at a time, in order. Type every code example yourself and run it. Do not just read. Each section has the same layout:

1. **Definition** (what it is, in plain words)
2. **Why we need it**
3. **Syntax**
4. **Example with output**
5. **Important points** (things to remember)
6. **Common mistakes**

**New:** Look for the **Flow of the code** blocks. They show, step by step, which line Python runs first, what happens next, and where each printed line comes from. Read the flow with the code open next to it.

**Two ideas that explain most flow confusion:**
- Python reads the file **top to bottom**. A `class` block only *stores* the blueprint. Nothing inside it runs until you create an object or call a method.
- When Python sees a call like `f(x)`, it runs the function, and then that call is **replaced by the value the function returns**. Inner brackets run first: in `print(acc.get_balance())`, `get_balance()` runs first, then `print` shows the result.

---

## Table of Contents

0. [What is OOP and why does it exist](#0-what-is-oop-and-why-does-it-exist)
1. [Class and Object](#1-class-and-object)
2. [Constructor `__init__` and `self`](#2-constructor-__init__-and-self)
2A. [Print vs Return, and Code Outside the Class](#2a-print-vs-return-and-code-outside-the-class)
3. [Instance Variable vs Class Variable](#3-instance-variable-vs-class-variable)
4. [Three Types of Methods](#4-three-types-of-methods-instance-class-static)
5. [Encapsulation](#5-encapsulation)
6. [Inheritance](#6-inheritance)
7. [Polymorphism](#7-polymorphism)
8. [Abstraction](#8-abstraction)
9. [Magic (Dunder) Methods](#9-magic-dunder-methods)
10. [Composition (Has-A) vs Inheritance (Is-A)](#10-composition-has-a-vs-inheritance-is-a)
11. [Useful Built-in Functions for OOP](#11-useful-built-in-functions-for-oop)
12. [Cheat Sheet](#12-cheat-sheet)
13. [Top Interview Questions with Answers](#13-top-interview-questions-with-answers)
14. [Practice Problems](#14-practice-problems)

---

## 0. What is OOP and why does it exist

### Definition
**OOP (Object-Oriented Programming)** is a way of writing programs where you group related **data** and the **functions that work on that data** together into one unit called a **class**.

### The problem OOP solves
Imagine you write a program for a bank *without* OOP:

```python
# Without OOP: data and functions are separate
rahul_name = "Rahul"
rahul_balance = 5000

priya_name = "Priya"
priya_balance = 8000

def deposit(balance, amount):
    return balance + amount

rahul_balance = deposit(rahul_balance, 1000)
```

With 1000 customers you would need 2000 variables. It becomes messy and easy to make mistakes (for example, passing Priya's balance to Rahul's function by accident).

### With OOP
```python
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

rahul = Account("Rahul", 5000)
priya = Account("Priya", 8000)

rahul.deposit(1000)
print(rahul.balance)   # 6000
print(priya.balance)   # 8000 (not affected)
```

Each account keeps its own data and its own functions together. That is the whole idea.

### The 4 pillars of OOP (you will learn each one below)
| Pillar | One-line meaning |
|---|---|
| **Encapsulation** | Hide the inside details, give controlled access |
| **Inheritance** | A new class can reuse an existing class |
| **Polymorphism** | Same method name, different behavior |
| **Abstraction** | Show only what is needed, force a common structure |

---

## 1. Class and Object

### Definition
- **Class**: a blueprint or template. It describes what data and behavior something will have. It is not a real thing yet.
- **Object** (also called **instance**): a real thing created from the blueprint.

**Real-life analogy:** A house plan (blueprint) is the class. The actual houses built from that plan are objects. One plan can build many houses.

### Syntax
```python
class ClassName:          # class names use CapitalCase (Student, BankAccount)
    # body of the class
    pass

object_name = ClassName()   # creating an object
```

### Example
```python
class Dog:
    pass

d1 = Dog()
d2 = Dog()

print(d1)           # <__main__.Dog object at 0x000001...>
print(d1 == d2)     # False  (two different objects)
print(type(d1))     # <class '__main__.Dog'>
```

### Important points
- Creating an object is called **instantiation**.
- One class can create unlimited objects.
- Every object has its own memory location.
- Naming rule: class names use `CapitalCase`, variables and functions use `snake_case`.

### Common mistakes
- Forgetting the brackets: `d1 = Dog` (this does NOT create an object, it just gives another name to the class). Correct: `d1 = Dog()`.

---

## 2. Constructor `__init__` and `self`

### Definition
- **Constructor (`__init__`)**: a special method that Python runs **automatically** at the moment an object is created. We use it to set up the starting data of the object.
- **`self`**: a reference to **the current object**. It tells Python "I am talking about this particular object, not any other one."

### Why we need it
Without `__init__`, every object starts empty, and you would need to add data manually:

```python
d1 = Dog()
d1.name = "Rex"       # tedious and error-prone
d1.breed = "Labrador"
```

With `__init__`, data is set the moment the object is born.

### Syntax
```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
```

### Example
```python
class Dog:
    def __init__(self, name, breed):
        print("Object is being created...")
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Rex", "Labrador")     # __init__ runs automatically here
d2 = Dog("Milo", "Beagle")

print(d1.name)     # Rex
print(d2.name)     # Milo
d1.bark()          # Rex says Woof!
d2.bark()          # Milo says Woof!
```

**Output:**
```
Object is being created...
Object is being created...
Rex
Milo
Rex says Woof!
Milo says Woof!
```

### Flow of the code (step by step)
Python runs the Dog example in this order:

1. Python reads `class Dog:` and **stores the blueprint**. Nothing prints. The code inside `__init__` and `bark` does **not** run yet, it is only saved.
2. `d1 = Dog("Rex", "Labrador")` runs:
   - Python creates a new empty object.
   - Python automatically calls `__init__`, passing the new object as `self`, plus `name="Rex"` and `breed="Labrador"`.
   - `print("Object is being created...")` runs. **(Output line 1)**
   - `self.name = "Rex"` and `self.breed = "Labrador"` are saved inside the object.
   - The finished object is handed back, and the name `d1` now points to it.
3. `d2 = Dog("Milo", "Beagle")` repeats the same steps with new values. **(Output line 2)**
4. `print(d1.name)` goes to the object `d1`, reads `name`, and prints `Rex`.
5. `print(d2.name)` prints `Milo`.
6. `d1.bark()` calls `bark` with `self = d1`, so `self.name` is `"Rex"` and it prints `Rex says Woof!`.
7. `d2.bark()` does the same with `self = d2` and prints `Milo says Woof!`.

What memory looks like after step 3:
```
d1  --->  { name: "Rex",  breed: "Labrador" }
d2  --->  { name: "Milo", breed: "Beagle"   }
```
Each object has its own copy of the data. `self` is just how a method says "the object I was called on".

### How `self` works (very important)
When you write `d1.bark()`, Python secretly converts it to `Dog.bark(d1)`. So `d1` gets passed as `self`. That is why `self.name` inside `bark` means "d1's name".

```python
d1.bark()          # what you write
Dog.bark(d1)       # what Python actually does (same result)
```

### Why `self.name` and not just `name`?
```python
class Dog:
    def __init__(self, name):
        self.name = name      # stored on the OBJECT (lives as long as the object)
        greeting = "Woof"     # plain local variable (dies when __init__ finishes)

    def bark(self):
        print(self.name)      # works
        print(greeting)       # ERROR: NameError, greeting does not exist here
```

**Rule:** If you want other methods to use a value later, store it as `self.something`.

### Important points
- `__init__` has two underscores on each side.
- `self` must be the **first parameter** of every normal method.
- The name `self` is a convention (you could write `this`), but always use `self`.
- `__init__` should not `return` anything (it returns `None` automatically).
- You can give default values: `def __init__(self, name, age=1):`

### Common mistakes
- Forgetting `self` in the parameter list: `def bark():` gives `TypeError: bark() takes 0 positional arguments but 1 was given`.
- Writing `name = name` instead of `self.name = name` (nothing gets saved).
- Writing `_init_` (one underscore) or `__int__` (typo). It will silently not run.

---

## 2A. Print vs Return, and Code Outside the Class

This section answers three questions that confuse almost everyone:
1. What is `money` in `money = atm()`? Is it an object or a number?
2. When do I write `print(money)`, `print(money.something())`, or `print(money())`?
3. What is "outside the class", and why does printing usually happen there?

### Part 1: What does `money = atm()` mean?
Always look at the **right side of the `=`**. It decides what the variable holds.

| Right side of `=` | What the variable holds |
|---|---|
| `ATM(1234, 5000)` (class name + brackets) | The whole **object** |
| `my_atm.check_balance()` (method name + brackets) | Whatever the method **returns** (for example a number) |
| `my_atm.check_balance` (method name, no brackets) | The method itself (rarely what you want) |

So `money = atm()` means: "create an ATM object and call it `money`". **`money` is not an amount of money, it is the ATM machine.** A clearer name would be `my_atm`.

Two more things to know:
- Class names are written in CapitalCase (`ATM`), so `atm()` and `ATM()` are different names in Python.
- If your `__init__` needs a pin and a balance, then `atm()` with empty brackets fails:
  ```
  TypeError: __init__() missing 2 required positional arguments: 'pin' and 'balance'
  ```
  You must pass them: `ATM(1234, 5000)`.

### Part 2: Brackets or no brackets?
**Brackets mean "run it now". No brackets mean "just refer to the thing".**

```python
class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

money = ATM(1234, 5000)        # money is the OBJECT

print(money)                   # <__main__.ATM object at 0x000001...>   the object itself
print(money.balance)           # 5000   a variable: NO brackets
print(money.check_balance())   # 5000   a method: brackets, it runs and returns 5000
print(money.check_balance)     # <bound method ATM.check_balance of ...>   forgot the brackets
print(money())                 # ERROR: TypeError: 'ATM' object is not callable
```

| You wrote | What it means | Result |
|---|---|---|
| `print(money)` | Print the object itself | `<__main__.ATM object at 0x...>` (unless you wrote `__str__`) |
| `print(money.balance)` | Print a variable stored in the object | `5000` |
| `print(money.check_balance())` | Run the method, then print what it returned | `5000` |
| `print(money.check_balance)` | Print the method itself (forgot brackets) | `<bound method ...>` |
| `print(money())` | Run the object like a function | **Error** (objects are not functions) |

**Why does `money()` fail?** Because `money` is an object, not a function. Only functions and methods can be "called" with brackets. The one exception is if your class defines the special method `__call__` (see Section 9):

```python
class ATM:
    def __call__(self):
        return "You called the object like a function"

money = ATM()
print(money())     # You called the object like a function
```

**Quick rule for what to write after the dot:**
- It stores data (`balance`, `name`, `pin`): **no brackets**.
- It does something (`deposit`, `withdraw`, `check_balance`): **brackets**.
- The object itself (`money`): **no brackets**, never, unless the class has `__call__`.

Also remember: if `money` holds a **number** (because you wrote `money = my_atm.check_balance()`), then `money()` fails too, with `TypeError: 'int' object is not callable`. You cannot call a number.

### Part 3: `print` vs `return` inside a method
- **`print(x)`** shows `x` on the screen. It does not give the value to anyone.
- **`return x`** hands `x` back to the line of code that called the method. Nothing appears on screen unless someone prints it.

**Version A: the method returns**
```python
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance          # hands the value back

my_atm = ATM(5000)
x = my_atm.check_balance()           # nothing on screen, x now holds 5000
print(x)                             # 5000
print(my_atm.check_balance())        # 5000  (same thing, one line)
my_atm.check_balance()               # runs, returns 5000, but nothing shows on screen
```

**Version B: the method prints**
```python
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(self.balance)          # shows it, hands back nothing

my_atm = ATM(5000)
x = my_atm.check_balance()           # 5000 appears on screen right now
print(x)                             # None   (the method returned nothing)
print(my_atm.check_balance())        # prints 5000, then prints None (two lines!)
```

That last line is the classic beginner mistake: **printing a method that already prints**. You get the value and then an extra `None`.

**Rule of thumb**
- **Inside the class:** use `return` to give answers back. This keeps the method reusable.
- **Outside the class:** use `print` to show those answers.
- Exception: a method whose whole job is to display (like `show_details()` or a menu) can `print` inside and needs no `return`. Then just call it: `s1.show_details()`, without wrapping it in `print(...)`.

### Part 4: What is "outside the class"?
Look at the **indentation**:
- Code **indented under `class`** is *inside* the class. It only defines the blueprint and its methods.
- Code at the **far left edge** (no indentation), written after the class, is *outside* the class. It is called the **main program** or **driver code**.

The class only *describes* things. The outside code is where you **create objects, call methods, and print**.

```python
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return self.__balance


# -------- everything below is OUTSIDE the class (main program) --------
atm1 = ATM(1234, 5000)               # line A
print(atm1.check_balance())          # line B   -> 5000
result = atm1.withdraw(2000)         # line C
print(result)                        # line D   -> 3000
print(atm1.withdraw(9999))           # line E   -> Insufficient balance
```

**Flow of the code (step by step)**
1. Python reads from the top. At `class ATM:` it **stores the blueprint**. No method runs. Nothing prints.
2. **Line A:** `ATM(1234, 5000)` creates an object. `__init__` runs automatically and saves the pin and balance inside it. The name `atm1` points to that object.
3. **Line B:** inner brackets first. `atm1.check_balance()` runs and returns `5000`. The call is now replaced by its value, so the line behaves like `print(5000)`. **Output: `5000`**
4. **Line C:** `atm1.withdraw(2000)` runs. Is `2000 > 5000`? No. So the balance becomes `3000` and the method returns `3000`. The variable `result` now holds `3000`. Nothing appears on screen, because there is no `print`.
5. **Line D:** `print(result)` shows `3000`. **Output: `3000`**
6. **Line E:** `atm1.withdraw(9999)` runs. Is `9999 > 3000`? Yes. So it returns the text `"Insufficient balance"` and the balance stays `3000`. `print` shows that text. **Output: `Insufficient balance`**

Final output:
```
5000
3000
Insufficient balance
```

**A tidier way to write the outside part (used in real projects)**
```python
if __name__ == "__main__":
    atm1 = ATM(1234, 5000)
    print(atm1.check_balance())
```
This means "run these lines only when I run this file directly, not when another file imports it". You can ignore the details for now. Just know that the main program often lives under this line.

### The golden rules
1. `ClassName(...)` with brackets **creates an object**. Keep it in a variable: `my_atm = ATM(1234, 5000)`.
2. `object.variable` has **no brackets**. `object.method()` has **brackets**.
3. Never put brackets after the object itself (`my_atm()`), unless the class has `__call__`.
4. Methods should **`return`** answers. The main program **`print`s** them.
5. A method call is replaced by its return value. If the method has no `return`, you get `None`.
6. `print(my_atm)` only shows something readable if you write `__str__` (Section 9).

### Self-test
Assume the Version A `ATM` class above, and `my_atm = ATM(5000)`.
1. What is `my_atm`? **The ATM object.**
2. `y = my_atm.check_balance()`. What is `y`? **The number 5000.**
3. What does `print(my_atm())` do? **Error.** The object is not callable.
4. A method only has `print(self.balance)` and no `return`. What does `z = my_atm.that_method()` store in `z`? **`None`.**
5. What does `print(y())` do if `y` is `5000`? **Error.** A number is not callable.

---

## 3. Instance Variable vs Class Variable

### Definition
- **Instance variable**: belongs to **one object**. Every object has its own copy. Created with `self.x = ...` inside methods (mostly `__init__`).
- **Class variable**: belongs to the **class itself**. Written directly inside the class, outside all methods. **Shared** by all objects.

**Analogy:** In a school, each student's name and marks are *instance* variables (different for each student). The school's name is a *class* variable (same for everyone).

### Syntax
```python
class Student:
    school_name = "Delhi Public School"    # class variable (outside methods)

    def __init__(self, name, marks):
        self.name = name                    # instance variable
        self.marks = marks                  # instance variable
```

### Example
```python
class Student:
    school_name = "Delhi Public School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Rahul", 75)
s2 = Student("Priya", 90)

# Reading
print(s1.name)          # Rahul
print(s2.name)          # Priya
print(s1.school_name)   # Delhi Public School
print(s2.school_name)   # Delhi Public School

# Changing the class variable through the CLASS changes it for everyone
Student.school_name = "ABC School"
print(s1.school_name)   # ABC School
print(s2.school_name)   # ABC School
```

### Important points
- Access a class variable using `ClassName.variable` (recommended) or `object.variable`.
- Change a class variable using `ClassName.variable = ...`.

### Flow of the code (step by step)
1. Python reads `class Student:`. Because `school_name = "Delhi Public School"` sits directly in the class body (outside all methods), it is created **right now** as a class variable, one copy for the whole class. The methods are only stored.
2. `s1 = Student("Rahul", 75)`: `__init__` runs, so `s1` gets its **own** `name` and `marks`.
3. `s2 = Student("Priya", 90)`: same, `s2` gets its own `name` and `marks`.
4. `print(s1.name)` finds `name` inside `s1` and prints `Rahul`.
5. `print(s1.school_name)`: Python looks inside `s1` first. It is not there, so Python looks in the class `Student` and finds it. **Lookup order: object first, then class.**
6. `Student.school_name = "ABC School"` changes the **single shared copy**.
7. `print(s1.school_name)` and `print(s2.school_name)` both look up the class, so both show `ABC School`.

### The trap (asked in interviews)
If you assign through an **object**, Python does NOT change the class variable. It creates a **new instance variable** on that object that hides the class one:

```python
s1 = Student("Rahul", 75)
s2 = Student("Priya", 90)

s1.school_name = "XYZ School"     # creates a NEW instance variable only on s1

print(s1.school_name)      # XYZ School   (s1's own copy)
print(s2.school_name)      # Delhi Public School   (still the class value)
print(Student.school_name) # Delhi Public School
```

**Flow of the trap:**
1. `s1.school_name = "XYZ School"`: **assigning through an object always writes onto that object.** It does not touch the class. So `s1` now gets its own `school_name`, which hides the class one.
2. `print(s1.school_name)`: found inside `s1` first, prints `XYZ School`.
3. `print(s2.school_name)`: `s2` has no own copy, so Python falls back to the class and prints `Delhi Public School`.
4. `print(Student.school_name)`: the class value was never changed, prints `Delhi Public School`.

### Second trap: mutable class variables
```python
class Student:
    subjects = []                # class variable, a list (mutable)

s1 = Student()
s2 = Student()
s1.subjects.append("Maths")
print(s2.subjects)               # ['Maths']  <- s2 is affected too! (shared list)
```
**Fix:** Put mutable data (lists, dictionaries) inside `__init__` as instance variables:
```python
class Student:
    def __init__(self):
        self.subjects = []       # each student gets their own list
```

### Quick comparison
| | Instance variable | Class variable |
|---|---|---|
| Defined | Inside methods using `self.x` | Directly inside the class |
| Belongs to | One object | The class (shared) |
| Different per object? | Yes | No |
| Use for | Name, marks, balance | Bank name, tax rate, counters |

---

## 4. Three Types of Methods (Instance, Class, Static)

### Definition
A **method** is a function that lives inside a class. There are three kinds. The only difference between them is **what data they can reach**.

| Type | First parameter | Decorator | Can access |
|---|---|---|---|
| **Instance method** | `self` | none | One object's data (and class data) |
| **Class method** | `cls` | `@classmethod` | Class-level data only |
| **Static method** | nothing | `@staticmethod` | Neither (just a helper function) |

### How to choose (ask one question)
**"What data does this method need?"**
- Needs **one object's data** (like this student's marks)? Use an **instance method**.
- Needs **shared class data** (like the school name)? Use a **class method**.
- Needs **neither**, just takes input and gives output? Use a **static method**.

### Full example
```python
class Student:
    school_name = "Delhi Public School"      # class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # 1. INSTANCE METHOD: works on ONE student
    def show_details(self):
        print(f"{self.name} scored {self.marks} at {self.school_name}")

    # 2. CLASS METHOD: works on the CLASS (all students)
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # 3. STATIC METHOD: helper, needs no student and no class data
    @staticmethod
    def is_pass(marks):
        return marks >= 40


s1 = Student("Rahul", 75)
s2 = Student("Priya", 35)

s1.show_details()                    # Rahul scored 75 at Delhi Public School
Student.change_school("ABC School")  # changes it for EVERY student
s1.show_details()                    # Rahul scored 75 at ABC School
print(Student.is_pass(s2.marks))     # False
```

### Flow of the code (step by step)
1. Python reads the class. `school_name` is created as a class variable. The three methods are stored (nothing runs).
2. `s1 = Student("Rahul", 75)` and `s2 = Student("Priya", 35)`: `__init__` runs twice, one per student.
3. `s1.show_details()`: an **instance method**. Python passes `self = s1`, so it prints `Rahul scored 75 at Delhi Public School`.
4. `Student.change_school("ABC School")`: a **class method**. Python passes `cls = Student` (the class, not an object). `cls.school_name = new_name` changes the shared value for everyone.
5. `s1.show_details()` runs again. `self.school_name` is looked up (object first, then class) and now finds `ABC School`, so it prints `Rahul scored 75 at ABC School`.
6. `print(Student.is_pass(s2.marks))` runs from the inside out:
   - First `s2.marks` is read, giving `35`.
   - Then `Student.is_pass(35)` runs. This is a **static method**, so no `self` or `cls`. It returns `35 >= 40`, which is `False`.
   - Finally `print(False)` shows `False`.

### Instance method in detail
- Has `self`, so it knows which object called it.
- Called on an object: `s1.show_details()`.
- Can read and change that object's data.

### Class method in detail
- Has `cls` (the class itself), not `self`.
- Called on the class (or an object, but class is clearer): `Student.change_school("X")`.
- Cannot access `self.name` because there is no specific object.
- **Most common real use: alternate constructors** (another way to create an object):

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, text):
        # text looks like "Rahul-75"
        name, marks = text.split("-")
        return cls(name, int(marks))       # same as Student(name, int(marks))

s = Student.from_string("Rahul-75")
print(s.name, s.marks)     # Rahul 75
```

### Static method in detail
- Has neither `self` nor `cls`.
- It is just a normal function placed inside the class because it logically belongs there.
- Called as `ClassName.method()`.

```python
class Validator:
    @staticmethod
    def is_valid_pin(pin):
        return len(pin) == 4 and pin.isdigit()

print(Validator.is_valid_pin("1234"))   # True
print(Validator.is_valid_pin("12ab"))   # False
```

### `self` vs `cls` in one line
- `self` = "this particular object" (Rahul's `self` is Rahul).
- `cls` = "the class itself" (only one exists, so changing it affects everyone).

### Self-test
What type of method would each be?
1. `get_full_name()` joins a person's first and last name. **Instance** (needs this person's data)
2. `set_tax_rate()` changes the tax rate for all employees. **Class** (shared data)
3. `is_even(number)` checks if a number is even. **Static** (needs nothing from the class)

### Common mistakes
- Forgetting `@classmethod` or `@staticmethod` above the method.
- Trying to use `self.name` inside a class method or static method.
- Using a static method when you actually need class data (use class method then).

---

## 5. Encapsulation

### Definition
**Encapsulation** means two things:
1. **Bundling** data and the methods that use it together in one class.
2. **Hiding** the internal data so it cannot be changed directly from outside. Access happens only through methods you control.

**Analogy:** An ATM. You cannot reach inside and change the cash count. You can only use the buttons (deposit, withdraw) and the machine checks the rules before doing anything.

### Why we need it
Without hiding, anyone can break your data:

```python
class Account:
    def __init__(self):
        self.balance = 1000

acc = Account()
acc.balance = -99999        # nothing stops this, invalid data!
acc.balance = "hello"       # this also works, and breaks everything later
```

### Access levels in Python
Python has no strict "private" keyword like Java. It uses naming rules:

| Name style | Meaning | Enforced? |
|---|---|---|
| `balance` | **Public**. Anyone can use it | n/a |
| `_balance` | **Protected**. "Please don't touch from outside" (a polite hint) | No, only a convention |
| `__balance` | **Private**. Python renames it internally, so direct access fails | Mostly yes |

### Example: private variable
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance        # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())     # 1500

print(acc.__balance)         # ERROR: AttributeError (hidden from outside)
```

### Flow of the code (step by step)
1. `acc = BankAccount(1000)`: `__init__` runs and stores `1000` as the private variable `__balance` inside `acc`.
2. `acc.deposit(500)`: `amount > 0` is true, so the balance becomes `1500`. This method has no `return` and no `print`, so nothing appears on screen.
3. `print(acc.get_balance())`: inner call first. `get_balance()` returns `1500`. Then `print` shows `1500`.
4. `print(acc.__balance)`: outside the class, Python looks for a variable named `__balance` and cannot find it (inside the class it was secretly renamed). So you get `AttributeError`, and the program stops here.

The lesson: outside code can only reach the balance through the methods you wrote (`deposit`, `withdraw`, `get_balance`). That is how the class protects its data.

### What is really happening: name mangling
Python secretly renames `__balance` to `_BankAccount__balance`. So this works (but you should NEVER do it, it defeats the purpose):
```python
print(acc._BankAccount__balance)    # 1500
```
That is why we say private in Python is "mostly enforced": it stops accidents, not determined people.

### The Pythonic way: `@property`
Writing `get_balance()` works, but Python has a cleaner way. `@property` lets you call a method **without brackets**, like it was a normal variable, while still running your code behind the scenes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):                 # GETTER: runs when you READ acc.balance
        return self.__balance

    @balance.setter
    def balance(self, value):          # SETTER: runs when you WRITE acc.balance = ...
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value


acc = BankAccount(1000)
print(acc.balance)        # 1000  (no brackets, the getter ran)
acc.balance = 2000        # setter ran, value accepted
print(acc.balance)        # 2000
acc.balance = -5          # ValueError: Balance cannot be negative
```

**Flow of the property example:**
1. `acc = BankAccount(1000)`: `__init__` stores `1000` in `__balance`.
2. `print(acc.balance)`: Python sees that `balance` is a **property**, so it runs the getter method automatically (no brackets needed). The getter returns `1000`, and `print` shows it.
3. `acc.balance = 2000`: Python sees you are **assigning** to a property, so it runs the setter with `value = 2000`. `2000 < 0` is false, so it stores `2000`.
4. `print(acc.balance)`: the getter runs again and returns `2000`.
5. `acc.balance = -5`: the setter runs with `value = -5`. `-5 < 0` is true, so it does `raise ValueError`. The program stops here and the bad value is never saved.

### Read-only property
If you write only the getter and no setter, the value can be read but not changed:
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2

c = Circle(5)
print(c.area)      # 78.5
c.area = 100       # AttributeError: can't set attribute
```

### Important points
- Encapsulation = hide data + control access through methods.
- Use `__name` for private, `_name` for "internal use".
- Use `@property` so validation happens automatically.
- Validation (like "no negative balance") is the main benefit.

### Common mistakes
- Thinking `_name` (one underscore) is private. It is not enforced.
- Making variables private but then having no way to read them (add a getter or property).
- Only bundling data with methods but leaving variables public. That is not real hiding.

### Review of your ATM code
In your ATM program, `self.pin` and `self.balance` are public, so anyone can write `atm1.balance = 9999999` and skip your pin check. To use encapsulation properly, change them to `self.__pin` and `self.__balance`, and keep all access inside your methods.

---

## 6. Inheritance

### Definition
**Inheritance** lets a new class (**child / subclass**) automatically get all the variables and methods of an existing class (**parent / superclass**), and then add or change things.

**Analogy:** A child inherits features from parents but can also have their own.

### Why we need it
To avoid writing the same code again and again (reusability).

Without inheritance, `Dog` and `Cat` both repeat `name` and `eat()`. With inheritance, you write them once in `Animal`.

### Syntax
```python
class Parent:
    pass

class Child(Parent):      # put the parent's name in brackets
    pass
```

### Example
```python
class Animal:                          # parent
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):                     # child, gets everything from Animal
    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Rex")
d.eat()       # Rex is eating   (inherited from Animal)
d.bark()      # Rex says Woof!  (Dog's own method)
```

### Flow of the code (step by step)
1. Python stores `Animal`, then stores `Dog(Animal)`. The brackets tell Python: "if a method is not found in `Dog`, look in `Animal`."
2. `d = Dog("Rex")`: Python looks for `__init__` in `Dog`. There is none, so it goes up to `Animal` and finds it. It runs with `self = d` and sets `self.name = "Rex"`.
3. `d.eat()`: not in `Dog`, found in `Animal`. It runs and prints `Rex is eating`.
4. `d.bark()`: found directly in `Dog`. It prints `Rex says Woof!`.

**Lookup rule:** Python searches the child first, then the parent, then the grandparent, and so on. The first match wins.

### Method overriding
A child can **replace** a parent's method by writing a method with the **same name**.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):                 # overrides the parent's speak
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

Animal().speak()   # Some sound
Dog().speak()      # Woof
Cat().speak()      # Meow
```

### `super()`: calling the parent's version
`super()` gives access to the parent class. It is mostly used in two places:

**1. In `__init__`, so the parent sets up its part:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)       # parent handles 'name'
        self.breed = breed           # child handles 'breed'

d = Dog("Rex", "Labrador")
print(d.name, d.breed)    # Rex Labrador
```

**2. In an overridden method, to run the parent's code AND add more:**
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()                # runs parent's version first
        print("Dog barks")

Dog().speak()
# Animal makes a sound
# Dog barks
```

**Flow of `super().__init__` (the Dog with a breed):**
1. `d = Dog("Rex", "Labrador")`: Python finds `__init__` in `Dog` first (child wins) and runs it with `name="Rex"`, `breed="Labrador"`.
2. `super().__init__(name)`: Python **jumps up** into `Animal.__init__` using the same object. It sets `self.name = "Rex"`, then returns to `Dog.__init__`.
3. `self.breed = "Labrador"` runs.
4. `print(d.name, d.breed)` prints `Rex Labrador`.

**Flow of `super().speak()`:**
1. `Dog().speak()`: Python finds `speak` in `Dog` and starts running it.
2. `super().speak()`: jumps up into `Animal.speak`, which prints `Animal makes a sound`, then comes back.
3. The next line in `Dog.speak` runs and prints `Dog barks`.

**Important:** If a child defines its own `__init__` and forgets `super().__init__(...)`, the parent's `__init__` does NOT run, and the parent's variables will be missing.

### The 5 types of inheritance

**1. Single**: one parent, one child
```python
class A: pass
class B(A): pass
```

**2. Multilevel**: a chain (grandparent, parent, child)
```python
class A: pass
class B(A): pass
class C(B): pass       # C gets from B, and B got from A
```

**3. Hierarchical**: one parent, many children
```python
class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass
```

**4. Multiple**: one child, many parents
```python
class Father:
    def skills(self): print("Gardening")

class Mother:
    def skills(self): print("Cooking")

class Child(Father, Mother):
    pass

Child().skills()     # Gardening  (Father is listed first, so it wins)
```

**5. Hybrid**: a mix of the above (for example, multiple + hierarchical together).

### MRO (Method Resolution Order)
When several parents have the same method name, Python searches in a fixed order. You can see it:

```python
class A:
    def show(self): print("A")

class B(A):
    def show(self): print("B")

class C(A):
    def show(self): print("C")

class D(B, C):
    pass

D().show()          # B
print(D.mro())      # [D, B, C, A, object]
```
Python checks left to right: `D`, then `B`, then `C`, then `A`, then `object`. The first match wins.

### Important points
- Child gets all public and protected members of the parent.
- Private (`__x`) members are not directly available in the child.
- Every class in Python secretly inherits from the built-in `object` class.
- Use inheritance only for a real "**is-a**" relationship (a Dog **is an** Animal).

### Common mistakes
- Forgetting `super().__init__()` in the child.
- Using inheritance when "has-a" is the right idea (see Section 10).
- Making very deep inheritance chains (hard to understand and debug).

---

## 7. Polymorphism

### Definition
**Polymorphism** means "many forms". The **same method name** or operator can behave **differently** depending on the object.

**Analogy:** The word "play" means different things for a guitarist, a footballer, and an actor.

### Why we need it
You can write one piece of code that works with many different types of objects, without checking what type each one is.

### 7.1 Method overriding (most common)
```python
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()       # same line of code, different result each time
# Woof
# Meow
# Moo
```

**Flow of the code (step by step):**
1. Python stores the three classes `Dog`, `Cat`, `Cow`.
2. `animals = [Dog(), Cat(), Cow()]` creates three objects and puts them in a list.
3. The `for` loop runs three rounds:
   - Round 1: `animal` is the Dog object. `animal.speak()` runs `Dog.speak` and prints `Woof`.
   - Round 2: `animal` is the Cat object. The **same line** now runs `Cat.speak` and prints `Meow`.
   - Round 3: `animal` is the Cow object, and it prints `Moo`.

Python decides *which* `speak` to run **at the moment of the call**, based on which object is in `animal`. That is polymorphism.

### 7.2 Duck typing (Python's special style)
Python does not care what class an object belongs to. It only cares whether the object **has the method you are calling**. The saying is: *"If it walks like a duck and quacks like a duck, it is a duck."*

```python
class Duck:
    def sound(self): print("Quack")

class Robot:
    def sound(self): print("Beep")

def make_sound(thing):
    thing.sound()            # works on anything that has a sound() method

make_sound(Duck())   # Quack
make_sound(Robot())  # Beep
```
`Duck` and `Robot` share no parent class, and it still works.

### 7.3 Method overloading (Python is different from Java here)
In Java you can have many methods with the same name and different parameters. **Python does not support this.** If you write the same name twice, the **last one replaces the first**:

```python
class Calc:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):        # this REPLACES the one above
        return a + b + c

c = Calc()
print(c.add(1, 2, 3))    # 6
print(c.add(1, 2))       # ERROR: missing argument 'c'
```

**Python's way: default arguments or `*args`:**
```python
class Calc:
    def add(self, *numbers):
        return sum(numbers)

c = Calc()
print(c.add(1, 2))          # 3
print(c.add(1, 2, 3, 4))    # 10
```

### 7.4 Operator overloading
You can decide what operators like `+`, `==`, `<` mean for your own class using dunder methods (more in Section 9).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)      # (4, 6)   Python called p1.__add__(p2)
```

### Important points
- Polymorphism lets one interface work with many types.
- Python achieves it through overriding, duck typing, and operator overloading.
- True method overloading (same name, different parameters) does not exist in Python.

---

## 8. Abstraction

### Definition
**Abstraction** means showing only the essential idea and hiding the details. In code, we usually create an **abstract class**: a class that defines *what* methods must exist, but leaves *how* they work to the child classes.

**Analogy:** A driving licence rule says "every car must have a `start()` and a `stop()`". It does not say how each car does it.

### Why we need it
It forces every child class to follow the same structure. If a child forgets a required method, Python raises an error immediately.

### Syntax
```python
from abc import ABC, abstractmethod

class ParentName(ABC):            # inherit from ABC

    @abstractmethod               # marks the method as required
    def method_name(self):
        pass                      # no code here
```

### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                       # child MUST write this
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


c = Circle(5)
r = Rectangle(4, 6)
print(c.area())      # 78.5
print(r.area())      # 24

s = Shape()          # ERROR: Can't instantiate abstract class Shape
```

### Flow of the code (step by step)
1. Python stores `Shape` and remembers that `area` is a **required** method.
2. `c = Circle(5)`: Python checks that `Circle` wrote its own `area`. It did, so the object is created and `radius = 5` is saved.
3. `r = Rectangle(4, 6)`: same check passes, `length = 4` and `width = 6` are saved.
4. `print(c.area())`: inner call first. `3.14 * 5 ** 2` gives `78.5`, which `area` returns. Then `print` shows `78.5`.
5. `print(r.area())`: `4 * 6` gives `24`, printed.
6. `s = Shape()`: Python checks `Shape` and sees an abstract method with no real code. It **refuses to create the object** and raises `TypeError` before anything else happens.

### What happens if a child forgets the method?
```python
class Triangle(Shape):
    pass                      # did not write area()

t = Triangle()                # ERROR: Can't instantiate abstract class Triangle
                              # with abstract method area
```

### Important points
- You **cannot create an object** of an abstract class directly.
- Every child **must** implement all abstract methods, or it also becomes abstract.
- An abstract class can also contain normal (non-abstract) methods that children reuse.
- Abstraction (design contract) is different from encapsulation (data hiding). Do not mix them up.

### Where you will use this (your roadmap)
For data pipelines, you can make an abstract `ETLStep` class that forces every step to have `extract()`, `transform()`, and `load()`.

---

## 9. Magic (Dunder) Methods

### Definition
**Dunder** = **D**ouble **UNDER**score. These are special methods with names like `__init__` or `__str__`. You almost never call them yourself. **Python calls them automatically** when you use certain operations.

### Why we need them
They let your own objects behave like built-in Python things (printable, comparable, addable, countable).

### The most important ones
| Method | Python calls it when you write | Purpose |
|---|---|---|
| `__init__` | `Student("Rahul")` | Set up a new object |
| `__str__` | `print(obj)` or `str(obj)` | Friendly text for users |
| `__repr__` | typing `obj` in console, or inside lists | Exact text for developers |
| `__len__` | `len(obj)` | Return a length |
| `__eq__` | `a == b` | Define equality |
| `__lt__` | `a < b` | Define "less than" |
| `__add__` | `a + b` | Define addition |
| `__getitem__` | `obj[0]` | Allow indexing |
| `__call__` | `obj()` | Make object callable like a function |

### Example: without and with `__str__`
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Rahul", 75)
print(s)          # <__main__.Student object at 0x000001...>  (not helpful)
```
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

s = Student("Rahul", 75)
print(s)          # Student: Rahul, Marks: 75
```

### Flow of the code (step by step)
1. `s = Student("Rahul", 75)`: `__init__` runs and saves the name and marks.
2. `print(s)`: `print` needs text, but `s` is an object. So Python **automatically asks the object to turn itself into text** by calling `s.__str__()` behind the scenes.
3. Your `__str__` builds the string `"Student: Rahul, Marks: 75"` and **returns** it (it does not print).
4. `print` receives that string and shows it.

Without `__str__`, step 2 falls back to Python's default, which is the unhelpful `<__main__.Student object at 0x...>`. This is why `__str__` must **return** a string: `print` is the one that displays it.

### `__str__` vs `__repr__` (very common interview question)
- `__str__`: for **users**, readable and friendly.
- `__repr__`: for **developers**, precise, ideally shows how to recreate the object.
- If only `__repr__` is defined, `print()` uses it as well. If only `__str__` is defined, `repr()` does not use it.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

s = Student("Rahul", 75)
print(s)            # Rahul scored 75         (__str__)
print(repr(s))      # Student('Rahul', 75)    (__repr__)
print([s])          # [Student('Rahul', 75)]  (lists use __repr__)
```

### More examples
```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        return self.members[index]

t = Team(["A", "B", "C"])
print(len(t))        # 3
print(t[1])          # B
```

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x

print(Point(1, 2) == Point(1, 2))     # True
print(Point(1, 2) < Point(5, 0))      # True
```

Without `__eq__`, `Point(1, 2) == Point(1, 2)` would be `False`, because Python compares memory addresses by default.

### Important points
- Always return a **string** from `__str__` and `__repr__` (do not just `print` inside them).
- Dunder methods are called by Python. You just define them.

---

## 10. Composition (Has-A) vs Inheritance (Is-A)

### Definition
- **Inheritance ("is-a")**: a Dog **is an** Animal.
- **Composition ("has-a")**: a Car **has an** Engine. One class **contains** an object of another class.

### The test
Ask: "Is X a type of Y?"
- Yes: use **inheritance**.
- No, X just contains or uses Y: use **composition**.

### Example
```python
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
```

Writing `class Car(Engine)` would be wrong, because a Car is not a type of Engine.

### Flow of the code (step by step)
1. Python stores `Engine`, then `Car`.
2. `Car().start()` runs from the inside out. First `Car()` creates a Car object, and its `__init__` runs, which creates an `Engine()` object and saves it as `self.engine`. The Car now **contains** an Engine.
3. Then `.start()` is called on that Car. Inside, `self.engine.start()` runs, so Python jumps into `Engine.start` and prints `Engine started`.
4. Control returns to `Car.start`, and the next line prints `Car is ready to drive`.

The Car does not inherit from Engine. It simply holds one and asks it to do its part.

### Why composition is often preferred
- Easier to change (swap the engine without touching the car's family tree).
- Avoids deep, confusing inheritance chains.
- The design rule "**favor composition over inheritance**" is well known.

### Another example: a library
```python
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
```

---

## 11. Useful Built-in Functions for OOP

```python
class Animal: pass
class Dog(Animal): pass

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
```

---

## 12. Cheat Sheet

### The 4 pillars
| Pillar | Meaning | Key tool in Python |
|---|---|---|
| Encapsulation | Hide data, control access | `__private`, `@property` |
| Inheritance | Reuse a parent class | `class Child(Parent)`, `super()` |
| Polymorphism | Same name, different behavior | Overriding, duck typing, `__add__` |
| Abstraction | Force a common structure | `ABC`, `@abstractmethod` |

### Method types
| | `self` | `cls` | Decorator | Use for |
|---|---|---|---|---|
| Instance | yes | no | none | Object data |
| Class | no | yes | `@classmethod` | Class data, alternate constructors |
| Static | no | no | `@staticmethod` | Helper functions |

### Variable types
| | Where written | Shared? |
|---|---|---|
| Instance | `self.x = ...` in methods | No, one per object |
| Class | Directly inside class | Yes, one for all |

### Access levels
| Style | Meaning |
|---|---|
| `x` | Public |
| `_x` | Protected (convention only) |
| `__x` | Private (name-mangled) |

### Most-used dunder methods
`__init__`, `__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, `__add__`, `__getitem__`, `__call__`

---

## 13. Top Interview Questions with Answers

**1. What is the difference between a class and an object?**
A class is a blueprint. An object is a real instance created from that blueprint.

**2. What is `self`?**
A reference to the current object. It lets methods access that object's own data.

**3. What is `__init__`?**
The constructor. It runs automatically when an object is created and sets up its starting data.

**4. Difference between instance variable and class variable?**
An instance variable is unique to each object (`self.x`). A class variable is shared by all objects and defined directly in the class body.

**5. Difference between instance, class, and static methods?**
Instance methods take `self` and work on one object. Class methods take `cls` and work on class-level data. Static methods take neither and are just helper functions inside the class.

**6. What is encapsulation? How do you achieve it in Python?**
Bundling data with methods and hiding the data from direct outside access. In Python, we use `__private` variables and `@property` with getters and setters.

**7. Does Python have real private variables?**
Not truly. `__x` triggers name mangling (renamed to `_ClassName__x`), which prevents accidents but can still be bypassed.

**8. What is inheritance? Name its types.**
A child class reusing a parent class. Types: single, multilevel, hierarchical, multiple, hybrid.

**9. What is `super()`?**
It gives access to the parent class, mostly used to call the parent's `__init__` or an overridden method.

**10. What is MRO?**
Method Resolution Order: the order in which Python searches parent classes for a method. Check it with `ClassName.mro()`.

**11. What is method overriding?**
A child class defining a method with the same name as its parent to change its behavior.

**12. Does Python support method overloading?**
Not in the Java sense. The last definition replaces earlier ones. We use default arguments or `*args` instead.

**13. What is duck typing?**
Python cares about whether an object has the needed method, not what class it belongs to.

**14. What is an abstract class?**
A class (using `ABC`) with at least one `@abstractmethod`. It cannot be instantiated. Child classes must implement the abstract methods.

**15. Difference between `__str__` and `__repr__`?**
`__str__` is a readable message for users. `__repr__` is an unambiguous description for developers.

**16. Composition vs inheritance?**
Inheritance is "is-a" (Dog is an Animal). Composition is "has-a" (Car has an Engine). Prefer composition when the relationship is not truly "is-a".

**17. Abstraction vs encapsulation?**
Abstraction is about design: defining what must exist and hiding complexity. Encapsulation is about data protection: hiding variables and controlling access.

---

## 14. Practice Problems

Try each on your own before looking anything up.

**Level 1: Basics**
1. Create a `Book` class with `title`, `author`, `price`. Add a method `show()` that prints the details. Create 3 books.
2. Create a `Counter` class with a **class variable** `count` that increases every time a new object is created. (Hint: change `Counter.count` inside `__init__`.)

**Level 2: Methods and encapsulation**
3. Create a `BankAccount` with private `__balance`, methods `deposit`, `withdraw` (raise `ValueError` if insufficient), and a `balance` property. Add a class variable `bank_name` and a `@classmethod set_bank_name()`.
4. Create an `Employee` class with `@classmethod from_string("Rahul-50000")` that builds an employee from a string, and a `@staticmethod is_valid_salary(amount)`.

**Level 3: Inheritance and polymorphism**
5. Create `Vehicle` with `name` and `speed`. Create `Car` and `Bike` as children with their own `describe()` method. Use `super().__init__`.
6. Put a `Car`, `Bike`, and `Truck` in one list and call `describe()` on each using a loop.

**Level 4: Abstraction and composition**
7. Create an abstract `Shape` class with abstract `area()` and `perimeter()`. Implement `Circle`, `Rectangle`, `Triangle`.
8. Build a `Library` that contains `Book` objects (composition) with `add_book`, `remove_book`, and `search_by_title`.

**Level 5: Put it all together (matches your roadmap)**
9. Build an ETL skeleton:
   - Abstract class `ETLStep` with abstract `run()`.
   - Children `ExtractStep`, `TransformStep`, `LoadStep`.
   - A `Pipeline` class that holds a list of steps and runs them in order.
   - Add `__str__` to each step.

---

**Final tip:** OOP only becomes clear when you write code yourself. After reading each section, close the notes and write the example from memory. If you get stuck, that is exactly the part to re-read.
