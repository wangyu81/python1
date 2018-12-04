class MyClass(object):
    num_count = 0
    def __init__(self,name):
        self.name = name
        MyClass.num_count += 1
        print (self.name, MyClass.num_count)
    def __del__(self):
        #self.name = name
        MyClass.num_count -= 1
        print (self.name, MyClass.num_count)
    def test():
        print ("aa")
aa = MyClass("Hello")
bb = MyClass("World")
cc = MyClass("AAAA")

del aa
del bb
del cc
