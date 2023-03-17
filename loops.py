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