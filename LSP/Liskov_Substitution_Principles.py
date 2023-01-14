# LSP - Принцип подстановки Барбары Лисков

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

# нарушение принципа
#class Square(Rectangle):
#    def __init__(self, size):
#        Rectangle.__init__(self, size, size)

#    @Rectangle.width.setter
#    def width(self, value):
#        self._width = self._height = value

#    @Rectangle.height.setter
#    def height(self, value):
#        self._width = self._height = value

def using(rectangle):
    w = rectangle.width
    rectangle.height = 10
    expected = int(w * 10)
    print(f'Expected: {expected}, got {rectangle.area}')

rectangle = Rectangle(2, 3)
print(using(rectangle))
