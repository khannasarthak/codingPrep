# Inheritance
class Person:
    def __init__(self,name): # Constructor
        self.name = name

    def getName(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(Person): # inherits Person
    def isEmployee(self):
        return True

emp = Person('Sarthak1') # object of person
print (emp.getName(),emp.isEmployee())

newEmp = Employee('Sarthak2')
print (newEmp.getName(), newEmp.isEmployee())

# use issubclass (a,b) to see if class is derived from another or not
print (issubclass(Person,Employee))
print (issubclass(Employee,Person))
