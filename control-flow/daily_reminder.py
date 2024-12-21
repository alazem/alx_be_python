# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"'{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high-priority task. You should complete it as soon as possible.")
    case 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a medium-priority task that requires attention today.")
        else:
            print(f"'{task}' is a medium-priority task. Focus on it when possible.")
    case 'low':
        if time_bound == 'yes':
            print(f"'{task}' is a low-priority task. You can complete it later today.")
        else:
            print(f"'{task}' is a low-priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")