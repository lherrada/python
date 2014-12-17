class Dog(object):
    count = 0 # this is a class variable
    dogs = [] # this is a class variable

    def __init__(self, name):
        self.name = name #self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n): # this is an instance method
        print("{0} says: {1}".format(self.name, "woof! " * n))
    #@staticmethod
    def rollCall(n): #this is implicitly a class method (see comments below)
        print("There are {0} dogs.".format(Dog.count))
        if n >= len(Dog.dogs) or n < 0:
            print("They are:")
            for dog in Dog.dogs:
                print("  {0}".format(dog))
        else:
            print("The dog indexed at {0} is {1}.".format(n, Dog.dogs[n]))

fido = Dog("Fido")
fido.bark(3)
print type(Dog.rollCall)
print Dog.rollCall
rex = Dog("Rex")
Dog.rollCall(0)
