import time

class object1:
    def __init__(self,oraganisation,College,Community):
        self.organisation = oraganisation
        self.College = College
        self.Community = Community
    
    def display_info(self):
        print(self.organisation)
        print(self.College)
        print(self.Community)


class object2:

    def __init__(self,Employee,Books,Events):
        self.Employee = Employee
        self.Books = Books
        self.Events = Events
    
    def display_info(self):
        print(self.Employee)
        print(self.Books)
        print(self.Events)


obj1 = object1(oraganisation="Global Giving",College="JNTUH",Community="The Diamond")
obj2 = object2(Employee="Venu",Books="RICH DAD POOR DAD",Events="Donation Drive")

#create
obj1.display_info()
print()
obj2.display_info()
print()

# Update
obj1.organisation="Human Source Giving"
obj1.College = "CBIT"
print()
print("\nAfter Update:")
obj1.display_info()
#Read 
print(obj2.Books + " is Written by Robert")
print()
print()
#update
obj2.Books = "Harrypotter"
obj2.display_info()
print(obj2.Books + "is written by J.K")
obj2.display_info()
print()
print()
#del
#del obj1
#del obj2