import os
os.system("cls")

class car:
    def __init__(self, model, speed = 0, color = "white"):
        self.model = model
        self.speed = speed
        self.color = color

    def car_info(self):
        return f"Model -> {self.model}\nSpeed -> {self.speed}\nColor -> {self.color}"

    def up_speed(self, up:int):
        self.speed += up

    def change_color(self, rang):
        self.color = rang


car1 = car("Mclaren f1", 80)

print(car1.car_info())
car1.up_speed(50)
car1.change_color("blue")
print(car1.car_info())