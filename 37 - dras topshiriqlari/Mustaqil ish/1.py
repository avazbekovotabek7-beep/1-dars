import os
os.system("cls")

class Rectangle:
    def __init__(self, height, weidh):
        self.height = height
        self.weidh = weidh

    def get_height(self):
        return self.height

    def set_height(self, new):
        self.height = new

    def get_weidh(self):
        return self.weidh

    def set_weidh(self, new):
        self.weidh = new

    def get_area(self):
        return (self.height * self.weidh) / 2

    def Perimetr(self):
        return (self.height + self.weidh) * 2

    def get_info(self):
        return f"Bo'yi => {self.height}\nEni => {self.weidh}\nYuzasi => {self.get_area()}\nPerimetri => {self.Perimetr()}"

Tortburchak = Rectangle(7, 6)

print(Tortburchak.get_info())