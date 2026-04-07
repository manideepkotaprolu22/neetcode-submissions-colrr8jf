from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        # Write your code here
        return copy.copy(self)

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        # Write your code here
        return copy.copy(self)

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        # Write your code here
        cloned_shapes = []

        for shape in shapes:
            cloned_shapes.append(shape.clone())

        return cloned_shapes

square = Square(10)
another_square = square.clone()

rectangle = Rectangle(10, 20)
another_rectangle = rectangle.clone()

test = Test()
shapes = [square, rectangle, another_square, another_rectangle]
cloned_shapes = test.clone_shapes(shapes)


print(shapes is cloned_shapes)  
print(len(shapes) == len(cloned_shapes)) 
print(shapes[0] is cloned_shapes[0])  
print(shapes[0].get_length() == cloned_shapes[0].get_length())  
