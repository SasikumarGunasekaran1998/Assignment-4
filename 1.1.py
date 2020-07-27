class side:  
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
class Area(side):
    def area(self):
        s = (self.a+self.b+self.c)/2
        a = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return a
    
if __name__ == "__main__":
    x = Area(2,4,3)
    print(x.area())
