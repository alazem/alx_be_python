import os

def file_exists_and_not_empty(file_path):
    """
    Checks if a given file exists and is not empty.
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        print("File exists and is not empty.")
    else:
        print("File does not exist or is empty. Ensure your script is saved correctly.")

def display_menu():
    """
    Displays the menu to the user.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print()

def main():
    """
    Main function to manage the shopping list.
    """
    # Array implementation for the shopping list
    shopping_list = []

    while True:
        # Call display_menu
        display_menu()

        try:
            # Input validation: Ensure the choice is a number
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                # Add an item
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to the shopping list.")
                else:
                    print("Item name cannot be empty.")

            elif choice == 2:
                # Remove an item
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' is not in the shopping list.")

            elif choice == 3:
                # View the list
                if shopping_list:
                    print("\nCurrent Shopping List:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")
                else:
                    print("The shopping list is currently empty.")

            elif choice == 4:
                # Exit the program
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # Example path to check if the script is saved correctly
    file_path = "/tmp/correction/4168825851415482759771672453448469848505_5/100741/992164/fns_and_dsa/shopping_list_manager.py"
    file_exists_and_not_empty(file_path)
    main()

