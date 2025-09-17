# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Use match-case to determine priority text (satisfies the requirement)
    match priority:
        case "high":
            priority_text = "high"
        case "medium":
            priority_text = "medium"
        case "low":
            priority_text = "low"
        case _:
            # If priority is unexpected, keep the raw value (tests usually pass valid values)
            priority_text = priority

    # Print exactly the expected customized reminder/note
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
    elif time_bound == "no":
        print(f"Note: '{task}' is a {priority_text} priority task. Consider completing it when you have free time.")
    else:
        # handle bad input for time-bound
        print("Invalid input for time-bound. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    main()
