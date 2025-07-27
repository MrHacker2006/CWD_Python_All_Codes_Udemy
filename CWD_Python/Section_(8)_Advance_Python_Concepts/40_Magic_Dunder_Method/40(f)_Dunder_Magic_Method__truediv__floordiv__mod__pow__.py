class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __truediv__(self, other):
        return(self.x/ other.x, self.y/ other.y )
    
    def __floordiv__(self, other):
        return(self.x// other.x, self.y// other.y )
    
    def __mod__ (self, other):
        return(self.x % other.x , self.y%other.y)
    
    def __pow__(self, other):
        return(self.x**other.x , self.y**other.y)
    

    
v1= vector(4,4)
v2= vector(4,4)
v3= vector(5,8)

# Using it for __truediv__
# v4 = v1/v2
# print(v4)

# Using it for __floordiv__
# v5 = v3//v2   #(5,8)//(4,4)
# print(v5)

# Using it for mod
# v6 = v3 % v2
# print(v6)

#Using it for exponential operator
v7 = v1**v2
print(v7)