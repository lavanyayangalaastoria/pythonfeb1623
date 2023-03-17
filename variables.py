#variables are containers for storing data values
x = 5
y = "Helloworld"
print(x,y)
x = 4 
x = "Sally"
print(x)
#casting - converting from one datatype to another datatype.
x = str(5)
y = int(3)
z = float(3)
#type() function
print(type(x))
print(type(y))
print(type(z))
#string variables can be declared either using single or double quotes
x = 'John'
y = "John"
print(x,y)


# variable names
#variable can have a short name like x or y or name etc..
#variable must start with letter or underscore
# variable names cannot start with numbers
# variable name can contain only alpha numeric char and underscore
#python is case sensitive age and AGE is different
#python cannot contain keywords
#legal variable names
myvar = "var"
my_var = "j"
_my_var = "varr"
MYVAR = "variablename"
print(myvar,my_var,_my_var,MYVAR)

my_var = "Hi"
my_var2 = "from John"
print(my_var + " "+ my_var2)

#types of variable names conventions

camelCase = "camelcaseconvention"
PascalCase = "PascalCaseConvention"
snake_case = "snakecase_convention"
print(camelCase,PascalCase,snake_case)

#assigning multiple values
x,y,z = "Orange","Banana","Cherry"
print(x,y,z)
#one value to multiple variables
x=y=z = "Orange"
print(x,y,z)

#unpack a collection
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x,y,z)

#output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "Is"
z = "Awesome"
print(x,y,z)
print(x+y+z)

x = 10
y = 5
print(x+y)