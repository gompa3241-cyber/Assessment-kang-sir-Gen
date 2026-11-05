
def stack_menu():
    letter_stack = []

    while True:
        print("\n================================")
        print("          STACK (LIFO)")
        print("================================")
        print("[1] Push Element")
        print("[2] Pop Element")
        print("[3] Display Stack")
        print("[4] Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            letter = input("Enter a letter: ").upper()

            if len(letter) == 1 and letter.isalpha():
                letter_stack.append(letter)
                print("Element pushed successfully!")
            else:
                print("Please enter only one letter.")

        elif choice == "2":
            if len(letter_stack) == 0:
                print("Stack is EMPTY!")
            else:
                removed = letter_stack.pop()
                print("Popped element:", removed)

        elif choice == "3":
            if len(letter_stack) == 0:
                print("Stack is EMPTY!")
            else:
                print("\nStack (Bottom to Top):", letter_stack)
                print("Top Element:", letter_stack[-1])

        elif choice == "4":
            print("Exiting Stack Program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    stack_menu()
