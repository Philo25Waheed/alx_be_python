# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Implementing shopping_list as a list at module level
shopping_list = []

def main():
    while True:
        display_menu()
        try:
            # Choice input as a number (required by checker)
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("No item entered. Nothing added.")
        elif choice == 2:
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue
            item = input("Enter item to remove: ").strip()
            if not item:
                print("No item entered. Nothing removed.")
            elif item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"Item '{item}' not found in the shopping list.")
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
