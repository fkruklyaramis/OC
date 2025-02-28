class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

rectangle = Rectangle(5, 3) 
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
