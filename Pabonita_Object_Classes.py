class Circle:
    def __init__(self, radius):
        self.radius = radius

# method to calculate the area
    def calculateArea(self):
        print(f"Area of the circle: {3.14 * self.radius ** 2}")

    def perimeter(self):
        print(f"Perimeter of the circle: {2 * 3.14 * self.radius}")


radius_value = 5
my_circle = Circle(radius_value)

my_circle.calculateArea()
my_circle.perimeter()
