class private:
    def __init__(self,name, url):
        self.name = name
        self.__url = url
    def who(self):
        print('name   :', self.name)
        print('url      :', self.__url)
    def __foo(self):
        print ('this is a private method')
    def foo(self):
        print ('this is a public method')
        self.__foo()
x = private('dic', 'www.to.com')
x.who()
#x.__foo
x.foo()
        
