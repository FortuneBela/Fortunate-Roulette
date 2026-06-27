import os
from pathlib import Path
from wheel import Wheel

wheel = Wheel()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")
 
curr_folder = Path.cwd()
child_folder = curr_folder / "Saved Roulettes"
child_folder.mkdir(exist_ok=True)

while True:
    clear_screen()

    print("\n-~= Fortunate Roulette =~-")
    print("1. Add Section")
    print("2. Remove Section")
    print("3. Edit Section")
    print("4. View Current Roulette")
    print("5. Spin Roulette")
    print("6. Save/Load Roulette")
    print("7. Exit")

    choice = input("Choose An Option: ").strip()

    if choice == "1":
        name = input("Please input a new Section: ").strip()
        
        if not name:
            print("Input cannot be empty.")
            pause()
        else:
            wheel.add_section(name)
            print(f"Added '{name}'")    
            pause()
    
    elif choice == "2":
        if wheel.is_empty():
            print("The Roulette is currently empty.")
            pause()
        else:
            print("~Your Current Roulette~")
            wheel.display(numbered=True)
            choice = input("\nPlease input section to remove: ").strip()
            if not choice.isdigit():
                print("Please enter a number instead.")
                pause()
            else:
                choice = int(choice)
                index = choice - 1

                if index < 0 or index >= len(wheel.sections):
                    print("Invalid Input")
                    pause()
                else:
                    removed_item = wheel.remove_section(index)
                    print(f"'{removed_item}' has been removed.")
                    pause()

    elif choice == "3":
        if wheel.is_empty():
            print("The Roulette is currently empty.")
            pause()
        else:
            print("~Your Current Roulette~")
            wheel.display(numbered=True)
            edit_choice = input("\nPlease input section to edit: ").strip()
            if not edit_choice.isdigit():
                print("Please enter a number instead.")
                pause()
            else:
                edit_choice = int(edit_choice)
                index = edit_choice - 1

                if index < 0 or index >= len(wheel.sections):
                    print("Invalid Input")
                    pause()
                else:
                    new_name = input("\nPlease enter a new name: ").strip()
                    if not new_name:
                        print("The new name cannot be empty.")
                        pause()
                    else:
                        old_name = wheel.edit_section(index, new_name)
                        print(f"'{old_name}' changed to '{new_name}'.")
                        pause()

    elif choice == "4":
        if wheel.is_empty():
            print("The Roulette is currently empty.")
            pause()
        else:
            print("~Your Current Roulette~")
            wheel.display(numbered=True)
            pause()

    elif choice == "5":
        result = wheel.spin()

        if result is None:
            print("The Roulette is empty!")
            pause()
        else:
            print("~Current Roulette~")

            wheel.display(numbered=True)

            print("Spinning...")
            print("Winner:", result)    
            pause()

    elif choice == "6":
        print("\n-=Data Management=-")
        print("1. Save Current Roulette")
        print("2. Load A Saved Roulette")
        print("3. Return To Main Menu")
        sl_choice = input("\nChoose an option. ").strip()

        if sl_choice == "1":
            name = input("Please enter the name you wish to save the file as: ").strip()
            
            if not name:
                print("Save name cannot be empty!")
                pause()
            else:
                filename = child_folder / f"{name}.json"
                wheel.save(filename)
                print(f"{name} saved!")
                pause()

        elif sl_choice == "2":
            print("-Saved Roulettes-\n")

            saved_roulettes = sorted(child_folder.glob("*.json"))

            if not saved_roulettes:
                print("No saved roulettes found.")
                pause()
            else:
                for index, file in enumerate(saved_roulettes, start=1):
                    print(f"{index}. {file.stem}")

                load_choice = input("\nPlease choose the number of which roulette to load: ").strip()
            
                if not load_choice.isdigit():
                    print("Please enter a number instead.")
                    pause()
                else:
                    load_choice = int(load_choice)
                    index = load_choice - 1
            
                    if index < 0 or index >= len(saved_roulettes):
                        print("Invalid Input")
                        pause()
                    else:
                        filename = saved_roulettes[index]
                        wheel.load(filename)
                        print(f"{filename.stem} Loaded!")
                        pause()
 
        elif sl_choice == "3":
            print("Returning To Main Menu...")
            pause()

        else:   
            print("Invalid Option")
            pause()

    elif choice == "7":
        print("Thank you for using Fortunate Roulette!")
        break

    else:
        print("Invalid Option")
        pause()