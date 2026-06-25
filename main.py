import random
import json
import os

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
    
wheel = Wheel()

while True:

    print("\n-~= Fortunate Roulette =~-")
    print("1. Add Section")
    print("2. Remove Section")
    print("3. View Current Roulette")
    print("4. Spin Roulette")
    print("5. Save Current Roulette")
    print("6. Load Saved Roulette")
    print("7. Exit")

    choice = input("Make your selection: ").strip()

    if choice == "1":
        name = input("Please input a new Section: ").strip()
        
        if name == "":
            print("Input cannot be empty.")
        else:
            wheel.add_section(name)
            print(f"Added '{name}'")    
    
    elif choice == "2":
        if wheel.is_empty:
            print("The Roulette is currently empty.")
        else:
            print("~Your Current Roulette~")
            wheel.display(numbered=True)
            choice = input("\nPlease input section to remove: ").strip()
            if not choice.isdigit():
                print("Please enter a number instead.")
            else:
                choice = int(choice)
                index = choice - 1

                if index < 0 or index >= len(wheel.sections):
                    print("Invalid Input")
                else:
                    removed_item = wheel.remove_section(index)
                    print(f"'{removed_item}' has been removed.")

    elif choice == "3":
        if wheel.is_empty:
            print("The Roulette is currently empty.")
        else:
            print("~Your Current Roulette~")
            wheel.display(numbered=True)

    elif choice == "4":
        result = wheel.spin()

        if result is None:
            print("The Roulette is empty!")
        else:
            print("~Current Roulette~")

            wheel.display(numbered=True)

            print("Spinning...")
            print("Winner:", result)    

    elif choice == "5":
        name = input("Please enter the name you wish to save the file as: ").strip()
        filename = f"{name}.json"
        wheel.save(filename)

    elif choice == "6":
        name = input("Please enter the name of the file you wish to load: ").strip()
        filename = f"{name}.json"
        if os.path.exists(filename):
            print("File Found!")
            wheel.load()
        else: 
            print("File Not Found.")
        

    elif choice == "7":
        print("Thank you for using Fortunate Roulette!")
        break

    else:
        print("Invalid selection")