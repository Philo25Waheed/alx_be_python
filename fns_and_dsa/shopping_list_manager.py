# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# shopping_list implemented at module level (array/list)
shopping_list = []

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))  # choice input as a number
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: '{item}'")
            else:
                print("No item entered. Nothing added.")
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
            elif not item:
                print("No item entered. Nothing removed.")
            else:
                if item in shopping_list:
                    shopping_list.remove(item)  # use list.remove()
                    print(f"Removed: '{item}'")
                else:
                    print(f"Item '{item}' not found.")
        elif choice == 3:
            if shopping_list:
                print("\nCurrent shopping list:")
                for idx, itm in enumerate(shopping_list, start=1):
                    print(f"{idx}. {itm}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
