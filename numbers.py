#numbers in python
print("numbers in python")

# there are three numeric types in python.
# 1 int
# 2 float
# 3 complex
# variables of numeric types are created when you assign a value to them.

x = 1 #int
y = 2.8 #float
z = 1j #complex
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
print("1. int")
# 1 int
x = 1
y = 33333
z = -1111
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
print("2.float")
# 2 float 
x = 1.10 
y = 1.0 
z = -35.59
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
print("Float can also be scientific numbers with 'e' which indicates power of 10")
x = 35e3
y = 12E4
z = -87.7e100
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
print("3. Complex")
x = 3 + 5j
y = 5j
z = -5j
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
print("Type Conversion")
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x,y,z)
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,10))
print("Casting in nums 1.int")
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
print("Casting in nums 2.float")
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z,w)
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print("Casting 3.string")
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))