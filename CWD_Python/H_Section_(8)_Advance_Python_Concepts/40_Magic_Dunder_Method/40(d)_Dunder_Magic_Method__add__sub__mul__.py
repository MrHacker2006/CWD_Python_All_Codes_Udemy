class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return(self.x - other.x , self.y - other.y)
    
    def __mul__(self, scaler):
        return(self.x*scaler, self.y*scaler)
    
    def __eq__(self, value):
        return(self.x==value, self.y==value)

v1 = vector(4,4)
v2 = vector(4,4)
v3 = v1 + v2
print(v3)

v4 = v1-v2
print(v4)
        
v5 = v1*5
print(v5)

print(v1==v2)