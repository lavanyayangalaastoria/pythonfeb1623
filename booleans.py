print("Boolean values")
print(10 > 9)
print(10 == 9)
print(10 < 9) 
a = 200
b = 33
print("--example two--")
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
  
print("Evaluate string and a number:")
print("--bool() funcn allows to evaluate any value - returns true or false in return--")
print(bool("Hello"))
print(bool(15))

print("Evaluate two variables:")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print("--Most values are True:-- ")
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print("--Most values are false: --")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}) )
print("One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:")
class myclass():
  def __len_(self):
    return 0 
myobj = myclass()
print(bool(myobj))
print("--functions can return boolean--")
def myFunction() :
  return True

print(myFunction())
print("print 'YES!' if the function returns True, otherwise print 'NO!' ")
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 
  
  
  
#Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) 