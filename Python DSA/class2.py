class MyClass:

    __hiddenVariables = 10 # using __ before variable names makes then hidden from the outside

    def add(self,increment):
        self.__hiddenVariables += increment
        print (self.__hiddenVariables)

myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
# print (myObject.__hiddenVariables) # gives an error

# However we can still acccess the variables using the following syntax

print (myObject._MyClass__hiddenVariables)
