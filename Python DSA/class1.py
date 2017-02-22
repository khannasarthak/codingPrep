class Test:

    place = 'India' # Class variable

    def __init__ (self,name): # Constructor
        self.name = name    # Instance variables

    def Say(self):
        print ('Hello ', self.name)

        # Adds an instance variable
    def setAddress(self, address):
        self.address = address

    # Retrieves instance variable
    def getAddress(self):
        return self.address

p = Test('Sarthak')
p.Say()
print(p.place)
p.setAddress('USA')
print (p.getAddress())
