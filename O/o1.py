

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self,radius):
        self.area1=(radius**2)*3.14

class Square(Shape):
    def area(self,side ):
        self.area1=side**2

class Rectangle(Shape):
    def area(self,side1,side2):
        self.area1=side1*side2


# c=Rectangle()
# c.area(5,6)
# print(c.area1)