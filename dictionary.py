# Creating a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#referring value of key in dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(len(thisdict))
# different datatypes in a dictionary
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict.keys()
print(x)


print(thisdict)
print(type(thisdict))
# dict() constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.keys()
print(x)
# # dictionary with keys and values of different data types
# numbers = {1: "One", 2: "Two", 3: "Three"}
# print(numbers)
#
# O/P: [3 : “Three”, 1: “One”, 2: “Two”]
#
# #Add Elements to a Python Dictionary
# capital_city = {"Nepal": "Kathmandu",
# "England": "London"}
# print("Initial Dictionary: ",capital_city)
# capital_city["Japan"] = "Tokyo"
# print("Updated Dictionary: ",capital_city)
#
# O/P: Initial Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London'}
# Updated Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London', 'Japan': 'Tokyo’}
#
# #Accessing Elements from Dictionary
# student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
#
# print(student_id[111])  # prints Eric
# print(student_id[113])  # prints Butters
# changing item referring to its key name
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

