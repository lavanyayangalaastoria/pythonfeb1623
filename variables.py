x = 5
y = "Helloworld"
print(x,y)
#casting
x = str(5)
y = int(3)
z = float(3)
#type() function
print(type(x))
print(type(y))
print(type(z))
#python is case sensitive
# char can be created using single or double quotesk

# variable names
# variable names cannot start with numbers
my_var = "Hi"
my_var2 = "from John"
print(my_var + " "+ my_var2)

#types of variable names conventions

camelcase = "camelcaseconvention"
PascalCase = "PascalCaseConvention"
snake_case = "snakecase_convention"
print(camelcase,PascalCase,snake_case)

#assigning multiple values
x,y,z = "Orange","Banana","Cherry"
print(x,y,z)
x=y=z = "Orange"
print(x,y,z)

#unpack a collection
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x,y,z)

#output variables
x = "Python is awesome"
print(x)