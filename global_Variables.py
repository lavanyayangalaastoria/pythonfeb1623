# variables created outside a function called as global variables.
# they can be used by everyone inside and outside of a function
# local variables are variables which are within the function where variables have been declared.
# global variables - entire program

a = 20
def display():
    a = 50
    print("Local value is",a)
display()
print("Global value is",a)

x = "awesome"
def myfunc():
    x = "hi"
    print("Python is: " +x)
myfunc()
print("Python is: " +x)

x = "object oriented"
def myfunc():
    print("Python is  "+x)
myfunc()
