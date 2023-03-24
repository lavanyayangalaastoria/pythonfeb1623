#datatypes
# Python has the following data types built-in by default, in these categories:
# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType
# getting type of datatype
#string
print("Print the datatype of the variable 'x', 'y' ")
x = 'hello'
y = "Hello"
print(x,y)
print(type(x))
x = 5 
print(x,type(x))
print(" -- # to specify the datatype use constructor functions -- ")
print("-- str example --") 
x = str("Hello world")
print(x)
x = "Hello World" 

print("x is:",x)
print("-- #int  -- ")	
x = 20 	
print("x is:",x)
print(" -- #float --")	
x = 20.5 	 
print("x is:",x)
print(" -- #complex --")	
x = 1j 	 
print("x is:",x)	
print(" -- #list --")
x = ["apple", "banana", "cherry"] 	
print("x is:",x)	
print(" -- tuple -- ")
x = ("apple", "banana", "cherry") 	
print("x is:",x) 
print("-- range() --")	
x = range(6) 		
print("x is:",x)
print(" -- dict -- ")
x = {"name" : "John", "age" : 36} 	
print("x is:",x)	
print(" -- set -- ")
x = {"apple", "banana", "cherry"} 	
print("x is:",x)	
print(" -- frozenset -- ")
x = frozenset({"apple", "banana", "cherry"})
print("x is:",x)	
print(" -- bool -- ")
x = True 		
print("x is:",x)
print(" -- bytes --")
x = b"Hello" 	
print("x is:",x)
print(" -- #bytearray --")	
x = bytearray(5) 		
print("x is:",x)
print("-- #memoryview  -- ")
x = memoryview(bytes(5)) 	
print("x is:",x)	
print("-- #NoneType -- ")
x = None 	 	
print("x is:",x)


