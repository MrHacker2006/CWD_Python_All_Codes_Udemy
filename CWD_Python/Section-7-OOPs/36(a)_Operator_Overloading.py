class Point:
    
    def __init__(self, x, y):  # Constructor to accept arguments
        self.x = x
        self.y = y

    def print_point(self):
        print(f"x is {self.x} and y is {self.y}")

    def sum(self, p):
       return Point((self.x + p.x), (self.y + p.y))
    
    
p1 = Point(3,6)
p2 = Point(2,5)

p = p1.sum(p2)
p.print_point()