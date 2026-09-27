

# ####################################################### Creating own data types ########################################################

# # There is no datatype for handing fractions in python, even no langauge has a data type to handle fractions. 

# '''
# # Creating fractions datatype using a class to handle various fraction maths operations like, 
#     - Addtion of fraction 
#     - Subtraction of fraction
#     - multiplication of fraction
#     - division of fraction

# '''

# #########################################################################################################################################

# class fraction:

#     def __init__(self, num, den):
#         self.n = num
#         self.d = den

# frac = fraction(3,4)
# print(type(frac))      # -> <class '__main__.fraction'>
       
# l = [1,2,3,4,frac]
# print(l)         # -> [1, 2, 3, 4, <__main__.fraction object at 0x10543a6c0>] -> as it does know how to display the frac.
#                     # it just shows frac is stored at this memory location. 


# ########################################################

# class fraction:

#     def __init__(self, num, den):
#         self.n = num
#         self.d = den

#     def __str__(self):
#         return "{}/{}".format(self.n, self.d)

# frac = fraction(4, 5)
# print(frac)    # -> prints 4/5 

# l = [1, 2, 3, 4, 5 ,frac]
# print([l])  # still show memory location instead of fraction 

# # ---------------------------------------------------------------------------

#                             # __str__ vs __repr__

# # __str__: Meant to be readable and clean for the end-user (e.g., print(frac))
# # __repr__: Meant to be unambiguous for debugging (e.g., inside collections like lists, tuple, dictionaries).

# # print(frac) triggers __str__ → "Show this to the user.
# # print([frac]) triggers __repr__ → "Show this inside a list.

# # ---------------------------------------------------------------------------

# class fraction:

#     def __init__(self, num, den):
#         self.n = num
#         self.d = den

#     def __str__(self):
#         return "{}/{}".format(self.n, self.d)

#     def __repr__(self):          # -> It tells Python how to display the object when it is hidden inside a collection like a list, tuple, or dictionary.
#         return self.__str__()

# frac = fraction(4, 5)
# print(frac)

# l = [1, 2, 3, 4, 5 ,frac]
# print(l)


# ########################################################

# --- Additon ---

class fraction:

    def __init__(self, num, den):
        self.n = num
        self.d = den

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    def __repr__(self):       
        return self.__str__()

    def __add__(self, other):  # -> here self is x having both num and deno, and other is y having both num and deno.

        temp_num = self.n * other.d + self.d * other.n
        temp_den = self.d * other.d

        return "{}/{}".format(temp_num, temp_den)


x = fraction(4, 5)
y = fraction(5, 6)

print(x + y)      # -> if __add__ magic method not used then,  TypeError: unsupported operand type(s) for +: 'fraction' and 'fraction'