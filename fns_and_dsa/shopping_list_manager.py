def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    # ---- Check for implementation of array shopping_list ----
    shopping_list = []
    if not isinstance(shopping_list, list):
        print("Error: shopping_list must be a list.")
        return

    while True:
        # ---- Check for calling display_menu() ----
        display_menu()

        choice_input = input("Enter your choice (1-4): ")

        # ---- Check for implementation of Choice Input as a number ----
        if not choice_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        choice = int(choice_input)

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f'"{item}" has been added to the shopping list.')
            else:
                print("Item cannot be empty.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from the shopping list.')
            else:
                print(f'"{item}" not found in the shopping list.')

        elif choice == 3:
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
