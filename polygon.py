class Polygon:
    pass


class Triangle(Polygon):
    def __init__(self):

        while(1):
            self.s1 = int(input("Enter side 1 of triangle: "))
            self.s2 = int(input("Enter side 2 of triangle: "))
            self.s3 = int(input("Enter side 3 of triangle: "))
            if(self.s1 < 0 or self.s2 < 0 or self.s3 < 0):
                print("Length cannot be negative")
                continue
            break

        self.s = (self.s1+self.s2+self.s3)/2

    def area(self):
        return (self.s*(self.s-self.s1)*(self.s-self.s2)*(self.s-self.s3)**(1/2))


class Rectangle(Polygon):
    def __init__(self):
        while(1):
            self.l = int(input("Enter the lenght of the rectangle: "))
            self.b = int(input("Enter the breadth of the rectangle: "))
            if(self.l < 0 or self.b < 0):
                print("Length cannot be negative")
                continue
            break

    def area(self):
        return (self.l*self.b)


shape1 = Triangle()
print(f"The area is {shape1.area()}")
