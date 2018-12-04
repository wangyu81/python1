class Dog():
    """ Dog class"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print (self.name.title() + " is barking")
    def tongue(self):
        print (self.name.title() + " is toungue")
dog1 = Dog("Big dog", 2)
dog2 = Dog("Small dog", 1)

print ("I'm %s , and I'm %d" %(dog1.name.title(),dog1.age))
dog1.bark()
dog2.tongue()
