# # class Person:
# #     def __init__(self):
# #         self.name = "Jack Matte"
# #
# #     def bio(self):
# #         self.addr = "Bakers street, London"
# #         self.taxInfo = "HUAPK29971"
# #         self.contact = "01-777-523-342"
# #         print(self.addr, self.taxInfo, self.contact)
# #
# #     def interest(self):
# #         self.favFood = "Chinese"
# #         self.hobbies = "Python Programming"
# #         self.bloodGroup = "A+"
# #         print(self.favFood, self.hobbies, self.bloodGroup)
# #
# # obj = Person()
# # print(obj.name)
# # obj.bio()
# # obj.interest()
#
# # class ParentClass:
# #     string = "Python Programming Language"
# #     def display(self):
# #         return self.string
# # class ChildClass(ParentClass):
# #     pass
# # child = ChildClass()
# # print(child.display())
# # print("String length: ", len("Programming"))
# # print("List length: ", len(["Python", "Java", "C"]))
# # print("Dictionary length: ", len({"Name": "John", "Address": "Nepal"}))
# class Bank:
#     def __init__(self):
#         self.name = "lavanya"
#
#     def accountdetails(self):
#         self.bank = "dhana"
#         self.id = '98j'
#         print(self.bank, self.id)
#
#     def interests(self):
#         self.interest = 'playing'
#         self.task = 'go'
#         print(self.interest, self.task)
#
#
# obj = Bank()
# print(obj.name)
# obj.accountdetails()
# obj.interests()
# class Bank:
#     def __init__(self):
#         self.name = "lavanya"
#
#     def accountdetails(self):
#         self.bank = "dhana"
#         self.id = '98j'
#         print(self.bank, self.id)
#
#     def interests(self):
#         self.interest = 'playing'
#         self.task = 'go'
#         print(self.interest, self.task)
#
#
# obj = Bank()
# print(obj.name)
# obj.accountdetails()
# obj.interests()
#encapsulation
class Employee():
    def __init__(self,name,project):
        self.name = name
        self.project = project
    def work(self):
        print(self.name, 'is working on', self.project)

obj = Employee('hari','task')
print(obj)
obj.work()

class example_class:
    name = 'i'
list = ['l','l','o','p','i']
list.sort()
print(list)