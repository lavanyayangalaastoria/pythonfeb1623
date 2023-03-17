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
x = 'hello'
y = "Hello"
print(x,y)
print(type(x))
x = 5 
print(x,type(x))
# to specify the datatype use constructor functions
#ex: 
x = str("Hello world")
print(x)
x = "Hello World" 	#str 
print("x is:",x)	
x = 20 	#int 
print("x is:",x)	
x = 20.5 	#float 
print("x is:",x)	
x = 1j 	#complex 
print("x is:",x)	
x = ["apple", "banana", "cherry"] 	#list 
print("x is:",x)	
x = ("apple", "banana", "cherry") 	#tuple
print("x is:",x) 	
x = range(6) 	#range 	
print("x is:",x)
x = {"name" : "John", "age" : 36} 	#dict 
print("x is:",x)	
x = {"apple", "banana", "cherry"} 	#set 
print("x is:",x)	
x = frozenset({"apple", "banana", "cherry"})
print("x is:",x)#frozenset 	
x = True 	#bool 	
print("x is:",x)
x = b"Hello" 	#bytes 
print("x is:",x)	
x = bytearray(5) 	#bytearray 	
print("x is:",x)
x = memoryview(bytes(5)) 	#memoryview 
print("x is:",x)	
x = None 	#NoneType 	
print("x is:",x)
