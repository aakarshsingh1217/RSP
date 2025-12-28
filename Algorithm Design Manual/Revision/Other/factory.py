# Define common inteface

class Shape:
    def draw(self):
        raise NotImplementedError
    
# Implement concrete classes

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"
    
class Square(Shape):
    def draw(self):
        return "Drawing a square"
    
# Create factory

class ShapeFactory:
    # @staticmethod means "this method belongs to this
    # class, not any specific object"
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        if shape_type == "circle":
            return Circle
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")

# Use factory

# Client asks factory for circle
# Factory decides which class to instantiate
# Client only talks to interface (Shape)
# No Circle() or Square() in client code
shape = ShapeFactory.create_shape("circle")
print(shape.draw())