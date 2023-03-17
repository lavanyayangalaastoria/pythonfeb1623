#creating a tuple
thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)
print(len(thistuple))
#create a tuple with one item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
print(thistuple[2:5])
print(thistuple[2:])
print(thistuple[-4:-1])


x = ("apple", "banana", "cherry")
y = list(x)
print(y)
y[1] = "kiwi"
x = tuple(y)
print(x)
print(type(y))
print(type(x))

#1. Converting the tuple into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
print(y,type(y))
y.append("orange")
thistuple = tuple(y)
print(thistuple,type(thistuple))

# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple,type(thistuple))

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
print(y,type(y))
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # this will raise an error because the tuple no longer exists