# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # return current date for reuse

def calculate_future_date(current_date, days_to_add):
    """
    Calculate the future date after adding the specified number of days.
    
    Parameters:
        current_date (datetime): The starting date
        days_to_add (int): Number of days to add

    Prints the future date in YYYY-MM-DD format
    """
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer number of days.")

    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
