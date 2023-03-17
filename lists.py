# creating a list.
# list can be created using square brackets and mutable
first_list = ["apple", "banana", "cherry"]
print(first_list)
# list2 is an example of mixed data types.
list2 = [20,5.5,'Hello']
print(list2)
# list 3 is an example of nested list.
list3 = [['rani',2020],['sai',2020],['lavanya',2020]]
print(list3)

List2 = ["apple","banana","cherry","apple","cherry"]
print(len(List2))
print(List2)
List1 = ["apple","banana","cherry"]
print(List1)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(list1)
thislist = list(("apple", "banana")) # note the double round-brackets
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
    print("Yes 'apple' is in the fruits list")
List1 = ["apple","banana","cherry","apple","cherry"]
thislist[2] = 'changed'
print(thislist)
#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist)

#change range of items
thislist = ["apple" , "banana" ,"cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)





# Elements are accessed through indexes in a list and they start from 0
# nega.
# list4 = [20,5.5,'h']
# print(list4[0])
# print(list4[-1])