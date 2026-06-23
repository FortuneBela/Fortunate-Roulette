import random

class Wheel:
    def __init__(self):
        self.sections = []

    def add_section(self, name):
        self.sections.append(name)

    def spin(self):
        return random.choice(self.sections)
    
wheel = Wheel()

wheel.add_section("Mario")
wheel.add_section("Luigi")
wheel.add_section("Wario")
wheel.add_section("Waluigi")

print(wheel.spin())