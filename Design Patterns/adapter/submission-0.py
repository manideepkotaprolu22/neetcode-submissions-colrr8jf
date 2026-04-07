class Square:
    def __init__(self, sideLength=0.0):
        self.sideLength = sideLength

    def getSideLength(self) -> float:
        return self.sideLength
    
class SquareHole:
    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def canFit(self, square: Square):
        return self.sideLength >= square.getSideLength()

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getRadius(self):
        return self.radius

class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
      # Write your code here
      self.circle = circle

    
    def getSideLength(self) -> float:
      # Write your code here
      return  self.circle.radius * 2


squareHole = SquareHole(5)

square = Square(5)
print(squareHole.canFit(square))   # True

circle = Circle(5)
circleAdapter = CircleToSquareAdapter(circle)
print(squareHole.canFit(circleAdapter))  # False


    