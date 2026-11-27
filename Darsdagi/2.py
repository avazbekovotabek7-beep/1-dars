import os
os.system("cls")

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius

    def set_radius(self, new):
        self.radius = new

    def get_color(self):
        return self.color

    def set_color(self, new):
        self.color = new

    def get_area(self):
        return (self.radius * self.radius) * 3.14

    def circumferance(self):
        return (self.radius * 2) * 3.14

    def get_info(self):
        return f"Radius => {self.radius}\nColor => {self.color}\nYuzaso => {self.get_area()}\nUzunligi => {self.circumferance()}"

doira = Circle(7, "qizil")

print(doira.get_info())