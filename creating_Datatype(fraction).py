

####################################################### Creating own data types ########################################################

# There is no datatype for handing fractions in python, even no langauge has a data type to handle fractions. 

'''
# Creating fractions datatype using a class to handle various fraction maths operations like, 
    - Addtion of fraction 
    - Subtraction of fraction
    - multiplication of fraction
    - division of fraction

'''

#########################################################################################################################################

class fraction:

    def __init__(self, num, den):
        self.n = num
        self.d = den

frac = fraction(3,4)
print(type(frac))      # -> <class '__main__.fraction'>
       
list = [1,2,3,4,frac]
print(list)       # -> [1, 2, 3, 4, <__main__.fraction object at 0x10543a6c0>] -> as it does know how to display the frac
