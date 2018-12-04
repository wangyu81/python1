class X_property(object):
    class_name = "X_property"
    def __init__(self,x=0):
        self.x = x
        self.class_info()

    def class_info(self):
        print ('class var:', X_property.class_name)
        print ('instace var:', self.x)

    def change(self,x):
        self.x = x
        self.class_info()
    def change_class(self,name):
        X_property.class_name = name
        self.class_info()


aaa = X_property()
bbb = X_property()

aaa.change(3)
bbb.change(10)
aaa.change_class('aaa')
bbb.change_class('bbb')
