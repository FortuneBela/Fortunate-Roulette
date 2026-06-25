import os

from wheel import Wheel
    
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
        
        if not name:
            print("Input cannot be empty.")
        else:
            wheel.add_section(name)
            print(f"Added '{name}'")    
    
    elif choice == "2":
        if wheel.is_empty():
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
        if wheel.is_empty():
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
            wheel.load(filename)
        else: 
            print("File Not Found.")
        

    elif choice == "7":
        print("Thank you for using Fortunate Roulette!")
        break

    else:
        print("Invalid selection")