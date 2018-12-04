def abs1(x,y):
    return abs(x),abs(y)
class Ant:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.d_point()
        
    def yi(self,x,y):
        x,y = abs1(x,y)
       # self.x = x
       # self.y = y
        self.e_point(x,y)
        self.d_point()

    def e_point(self,x,y):
        self.x += x
        self.y += y

    def d_point(self):
        print ("Current position is %d , %d" %(self.x,self.y))


ant_a = Ant()
ant_a.yi(3,5)
ant_a.yi(2, -7)
