class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        return(self.x==value, self.y==value)
    
    def __ne__(self, value):
        return(self.x!=value, self.y!=value)
    
    def __lt__(self, value):
        return (self.x < value.x and self.y<= value.y)
    
    def __le__(self, value):
        return (self.x <= value.x and self.y<= value.y)
    #Similarily __ge__ 
    def __gt__(self,value):
        return(self.x > value.x and self.y > value.y)
    

v1= vector(4,4)
v2= vector(4,4)
v3= vector(5,8)


# For equal to 
# print(v1==v2)


#For not equal to 
# print(v1!=v2)
# print(v1!=v3)


#For less than
# print(v1 < v3) #True


#For less than equal to 
# print(v1<=v2)
# print(v1<=v3)
# print(v3<=v1)

#For greater than 
print(v3>v1)


