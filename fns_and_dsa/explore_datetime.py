from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user to enter a number of days and calculates the future date.
    """
    try:
        # Prompt the user to enter the number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Get the current date
        current_date = datetime.now()
        # Calculate the future date
        future_date = current_date + timedelta(days=number_of_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    """
    Main function to execute both parts of the task.
    """
    # Display the current date and time
    display_current_datetime()
    print()  # Add a blank line for better readability
    # Calculate a future date
    calculate_future_date()

if __name__ == "__main__":
    main()
