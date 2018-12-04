class Dog():
    "a dog class"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print (self.name.title() + "barking")
    def tongue(self):
        print (self.name.title() + "tongue")


dog1 = Dog("a little dog", 2)
print ("hello")
dog1.bark()
dog1.tongue()
