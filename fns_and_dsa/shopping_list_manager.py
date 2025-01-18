# Shopping List Manager Script

def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage the shopping list.
    """
    # Implementation of the shopping list as an array
    shopping_list = []

    while True:
        # Call the display_menu function
        display_menu()

        try:
            # User input for choice as a numeric option
            choice = int(input("\nEnter your choice (1-4): "))

            if choice == 1:
                # Add item to the shopping list
                item = input("Enter the item to add: ").strip()
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            elif choice == 2:
                # Remove item from the shopping list
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' not found in the list.")
            elif choice == 3:
                # Display the shopping list
                if shopping_list:
                    print("\nCurrent Shopping List:")
                    for index, item in enumerate(shopping_list, start=1):
                        print(f"{index}. {item}")
                else:
                    print("The shopping list is empty.")
            elif choice == 4:
                # Exit the program
                print("Exiting the Shopping List Manager. Goodbye!")
                break
            else:
                # Handle invalid numeric choices
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
