class Polygon:
    def __init__(self, numsides):
        self.n = numsides
        self.sides = []
        self.perim = 0.0

    def findPerim(self):
        for i in range(self.n):
            self.sides.append(float(input('enter the length of a side: ')))

            for item in self.sides:
                self.perim += item

            print('The perimeter is', str(self.perim))

    def dispSide(self):
        print('This polygon has %d sides' % len(self.sides))
        print('This polygon has sides has sides with lengths', self.sides)


    def __str__(self):
        self.dispSide()
        return('The perimeter is %.02f' % self.perim)

class Triangle(Polygon):
    def __init__(self, numsides = 3):
        Polygon.__init__(self, numsides)

    def findPerim(self):
        Polygon.findPerim(self)

    def dispSide(self):
        print('This triangle has %d sides' % len(self.sides))
        print('This triangle has sides with lengths', self.sides)
        print()

    def findArea(self):
        self.area = self.sides[0] * self.sides[1] * 0.5
        print('The area of the right triangle is', self.area)

class Hexagon(Polygon):
    def __init__(self, numsides = 3):
        Polygon.__init__(self, numsides)

    def findPerim(self):
        Polygon.findPerim(self)

    def dispSide(self):
        print('This hexagon has %d sides' % len(self.sides))
        print('This hexagon has sides with lengths', self.sides)
        print()

    def findArea(self):
        self.area = (self.sides[0] * self.sides[1] * 0.5) * 6
        print('The area of the hexagon is', self.area)

class Square(Polygon):
    def __init__(self, numsides = 3):
        Polygon.__init__(self, numsides)

    def findPerim(self):
        Polygon.findPerim(self)

    def dispSide(self):
        print('This square has %d sides' % len(self.sides))
        print('This square has sides with lengths', self.sides)
        print()

    def findArea(self):
        self.area = self.sides[0] * self.sides[1] 
        print('The area of the square is', self.area)

if __name__ == '__main__':

    shape = Polygon(3)
    shape.findPerim()
    shape.dispSide()
    print(shape)

    tri = Triangle(3)
    tri.findPerim()
    tri.dispSide()
    tri.findArea()
    print(tri)

    hexa = Hexagon(6)
    hexa.findPerim()
    hexa.dispSide()
    hexa.findArea()
    print(hexa)

    sqr = Square(4)
    sqr.findPerim()
    sqr.dispSide()
    sqr.findArea()
    print(sqr)
    
   
