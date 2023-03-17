print("Boolean values")
print(10 > 9)
print(10 == 9)
print(10 < 9) 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
  
print("Evaluate string and a number:")
  
print(bool("Hello"))
print(bool(15))

print("Evaluate two variables:")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print("Most values are True: ")
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print("Most values are false: ")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}) )

#functions can return boolean
def myFunction() :
  return True

print(myFunction())
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 
  
  
  
#Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) 