
def queue_menu():
    letter_queue = []

    while True:
        print("\n================================")
        print("          QUEUE (FIFO)")
        print("================================")
        print("[1] Enqueue Element")
        print("[2] Dequeue Element")
        print("[3] Display Queue")
        print("[4] Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            letter = input("Enter a letter: ").upper()

            if len(letter) == 1 and letter.isalpha():
                letter_queue.append(letter)
                print("Element enqueued successfully!")
            else:
                print("Please enter only one letter.")

        elif choice == "2":
            if len(letter_queue) == 0:
                print("Queue is EMPTY!")
            else:
                removed = letter_queue.pop(0)
                print("Dequeued element:", removed)

        elif choice == "3":
            if len(letter_queue) == 0:
                print("Queue is EMPTY!")
            else:
                print("\nFront ->", letter_queue, "<- Rear")

        elif choice == "4":
            print("Exiting Queue Program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    queue_menu()
