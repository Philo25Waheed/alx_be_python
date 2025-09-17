def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()
    
    is_time_bound = time_bound_input == 'yes'
    
    match priority:
        case "high":
            if is_time_bound:
                message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                message = f"Reminder: '{task}' is a high priority task. Make sure to complete it soon."
        case "medium":
            if is_time_bound:
                message = f"Reminder: '{task}' is a medium priority task that requires attention today."
            else:
                message = f"Note: '{task}' is a medium priority task. Consider completing it in the near future."
        case "low":
            if is_time_bound:
                message = f"Reminder: '{task}' is a low priority task, but it requires completion today."
            else:
                message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            message = "Invalid priority level. Please enter high, medium, or low."
    
    print("\n" + message)

if __name__ == "__main__":
    main()
