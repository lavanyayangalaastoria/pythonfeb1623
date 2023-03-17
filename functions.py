print(" --- Functions --- ")
print("--Creating a Function--")
def myfunction():
    print("2. my function is created")

def myfunction():
    print("my function is called")
myfunction()
print("--Passing Arguments--")
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("Passing 2 arguments")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") 