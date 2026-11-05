
MAX_SIZE = 6


def array_menu():
    letter_array = []

    while True:
        print("\n================================")
        print("       ARRAY / STATIC LIST")
        print("================================")
        print("[1] Insert Element")
        print("[2] Delete Element")
        print("[3] Display Array")
        print("[4] Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(letter_array) >= MAX_SIZE:
                print("Array is FULL!")
            else:
                letter = input("Enter a letter: ").upper()

                if len(letter) == 1 and letter.isalpha():
                    letter_array.append(letter)
                    print("Element inserted successfully!")
                else:
                    print("Please enter only one letter.")

        elif choice == "2":
            if len(letter_array) == 0:
                print("Array is EMPTY!")
            else:
                removed = letter_array.pop()
                print("Deleted element:", removed)

        elif choice == "3":
            print("\nCurrent Array:", letter_array)
            print("Current Size:", len(letter_array))
            print("Maximum Size:", MAX_SIZE)

        elif choice == "4":
            print("Exiting Array Program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    array_menu()
