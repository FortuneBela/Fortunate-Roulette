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
    
    def display(self, numbered=False):
        if numbered:
            for index, item in enumerate(wheel.sections, start=1):
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
    print("5. Exit")

    choice = input("Make your selection: ").strip()

    if choice == "1":
        name = input("Please input a new Section: ").strip()
        
        if name == "":
            print("Input cannot be empty.")
        else:
            wheel.add_section(name)
            print(f"Added '{name}'")    
    
    elif choice == "2":
        if not wheel.sections:
            print("The Roulette is currently empty.")
        else:
            print("~Your Current Roulette~")
            wheel.display(numbered=True)
            choice = input("\nPlease input section to remove: ").strip()
            choice = int(choice)
            index = choice - 1

            if index < 0 or index >= len(wheel.sections):
                print("Invalid input")
            else:
                removed_item = wheel.sections[index]
                wheel.sections.pop(index)
                print(f"'{removed_item}' has been removed.")

    elif choice == "3":
        if not wheel.sections:
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
        break

    else:
        print("Invalid selection")