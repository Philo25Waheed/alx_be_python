def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if not item:
        print("No item entered. Nothing was added.")
        return
    shopping_list.append(item)
    print(f"Added: '{item}'")

def remove_item(shopping_list):
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.")
        return

    item = input("Enter item to remove: ").strip()
    if not item:
        print("No item entered. Nothing was removed.")
        return

    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed: '{item}'")
        return

    lowered = item.lower()
    for existing in shopping_list:
        if existing.lower() == lowered:
            shopping_list.remove(existing)
            print(f"Removed (case-insensitive match): '{existing}'")
            return

    print(f"Item '{item}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
        return

    print("\nCurrent shopping list:")
    for idx, item in enumerate(shopping_list, start=1):
        print(f"{idx}. {item}")

def main():
    shopping_list = []
    try:
        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                add_item(shopping_list)
            elif choice == '2':
                remove_item(shopping_list)
            elif choice == '3':
                view_list(shopping_list)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!")

if __name__ == "__main__":
    main()
