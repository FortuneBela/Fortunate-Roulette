import random

class Wheel:
    def __init__(self):
        self.sections = []

    def add_section(self, name):
        self.sections.append(name)

    def spin(self):
        if not self.sections:
            return None
        
        return random.choice(self.sections)
    
wheel = Wheel()

while True:
    name = input("Please input a new result, or enter 'done' to finish: ").strip()
    if name.lower() == "done":
        break

    if name == "":
        print("Input cannot be empty.")
        continue
    wheel.add_section(name)

result = wheel.spin()

if result is None:
    print("The wheel is empty!")
else:
    print("-Current Wheel-")

    for item in wheel.sections:
        print(item)

    print("Spinning...")
    print("Winner:", result)