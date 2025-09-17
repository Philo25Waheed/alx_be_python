# daily_reminder.py

def main():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()
    
    # Check if time-bound
    is_time_bound = time_bound_input == 'yes'
    
    # Base message based on priority
    match priority:
        case "high":
            base_message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            base_message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            base_message = f"Note: '{task}' is a low priority task"
        case _:
            base_message = "Invalid priority level"
    
    # Modify message if time-bound using if statement (as required)
    if is_time_bound:
        if priority == "high":
            message = base_message + " that requires immediate attention today!"
        elif priority == "medium":
            message = base_message + " that requires attention today."
        elif priority == "low":
            message = base_message + ", but it requires completion today."
        else:
            message = base_message
    else:
        if priority == "low":
            message = base_message + ". Consider completing it when you have free time."
        else:
            message = base_message + "."
    
    print("\n" + message)

if __name__ == "__main__":
    main()
