def abs1(x,y):
    return (abs(x), abs(y))
class Ant():
    """ A class of Ant move"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.d_point()
    def d_point(self):
        print ("Current position: %d , %d" %(self.x,self.y))
    def e_point(self,x,y):
        self.x += x
        self.y += y
    def yi(self,x,y):
        x,y = abs1(x,y)
        self.e_point(x,y)
        self.d_point()



ant1 = Ant()
ant1.yi(3, 5)
ant1.yi(2,-7)
