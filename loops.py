print(" if condition")
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
print(" 2. elif")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("3.Else condition")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
print("OR operator")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
print("NOT Operator")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
print("Nested if statements")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
print("Pass statement")
a = 33
b = 200

if b > a:
  pass

print("No output as pass statement does nothing but acts as a placeholder")

print("While loop")
i = 1
while i < 6:
  print(i)
  i += 1
  
print("Break Statement")
print("Exit the loop when i is 3")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
  
print("Continue Statement")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
print("For Loop")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
print("Looping through a string")
for x in "banana":
  print(x)

print("Break Statement")
print("Exit the loop when x is 'banana'")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("Exit the loop when x is 'banana', but this time the break comes before the print:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
print("Continue Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
print("range() function")
for x in range(6):
    print(x)
for x in range(1,6):
    print(x)
    
print("Increment sequence by adding 3rd parameter")
for x in range(2, 30, 3):
  print(x)
  
print("Else in FOR Loop")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
print("Nested Loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 