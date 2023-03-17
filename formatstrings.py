print("format() method is usedd to pass arguments ,formmat them and add the values of parameter to the string - like placeholder{}")
age = 36
txt = "John's age is {}"
print(txt.format(age))
#format() method takes unlimited num of arguments and are placed to respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#format using index numbers
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))