import os
os.system("cls")

class Student1:
    def __init__(self, name, age, phoneN):
        self.box1 = name
        self.box2 = age
        self.box3 = phoneN

    def Student1_info(self):
        return f"Name -> {self.box1}\nAge -> {self.box2}\nPhoen_N -> {self.box3}"

Natija = Student1("Ali", 20, "+998123456")

print(Natija.Student1_info())
