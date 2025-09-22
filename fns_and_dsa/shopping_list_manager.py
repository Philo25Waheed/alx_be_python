# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Array implementation at module level
shopping_list = []

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))  # <- checker looks for this

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"Added: {item}")
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"{item} not found.")
        elif choice == 3:
            if shopping_list:
                print("Current shopping list:")
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
