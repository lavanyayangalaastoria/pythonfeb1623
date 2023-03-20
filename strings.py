# Strings in python are surrounded by either single quotation marks or double quotation marks.

# 'hello' is the same as "hello".
print("Hello")
print('Hello')
#assigning string to a variable
a = "Hello"
print(a)
#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
print("Strings are arrays")
a = "Hello, World!"
print(a[1])

print("Looping through a string")
for x in "banana":
    print(x)
print("len of string")
print(len(x))

print("Check string using in keyword")
txt = "The best things in life are free!"
print("free" in txt)
#using if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
print("IF NOT")
txt = "The best things in life are free!"
print("expensive" not in txt)

print("print only if 'expensive' is NOT present:")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")