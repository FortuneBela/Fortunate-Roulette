import random
import json

class Wheel:
    def __init__(self):
        self.sections = []

    def add_section(self, name):
        self.sections.append(name)

    def remove_section(self, index):
        return self.sections.pop(index)
    
    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(self.sections, file)

    def load(self, filename):
        with open(filename, "r") as file:
            self.sections = json.load(file)
    
    def is_empty(self):
        return len(self.sections) == 0

    def spin(self):
        if not self.sections:
            return None
        
        return random.choice(self.sections)
    
    def display(self, numbered=False):
        if numbered:
            for index, item in enumerate(self.sections, start=1):
                print(f"{index}. {item}")
        else:
            for item in self.sections:
                print(item)