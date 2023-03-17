#creating a set
Student_id = {112, 114, 116, 118, 115}
print('Student ID: ', Student_id)

# create a set of string type
Vowel_letters = {'a','e','i','o','u'}
print('Vowel Letters:', Vowel_letters)

# creating a set of mixed data types
Mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', Mixed_set)

#Duplicates Not Allowed
thisset = {"apple","banana","cherry","apple"}
print(thisset)
#add method
fruits = {"apple","banana","cherry"}
fruits.add("orange")
print(fruits)
# O/P : {"apple","banana","cherry“, “orange"}
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print('output of copy: ',x)
# O/P: {"apple", "banana", "cherry"}

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)




