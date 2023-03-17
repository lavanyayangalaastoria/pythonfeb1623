# variables created outside a function called as global variables.
# they can be used by everyone inside and outside of a function
# local variables are variables which are within the function where variables have been declared.
# global variables - entire program
#local and global declarations
#create a variable inside a function with same name
# as global variable.
a = 20
def display():
    a = 50
    print("Local value is",a)
display()
print("Global value is",a)
# create a variable inside a function with same name as global variable.
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
#use global keyword - the variable belongs to global scope
def myfunc():
    global x 
    x = "fantastic"
myfunc()
print("Python is "+x)

#use global keyword - to change global variable inside a function
x = "awesome"
def myfunc():
    global x 
    x = "fantastic"
myfunc()
print("Python is "+x)


