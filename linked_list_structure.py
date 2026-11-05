
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        print("Element inserted successfully!")

    def delete(self):
        if self.head is None:
            print("Linked List is EMPTY!")
        else:
            removed = self.head.data
            self.head = self.head.next
            print("Deleted element:", removed)

    def display(self):
        if self.head is None:
            print("Linked List is EMPTY!")
        else:
            current = self.head

            print("\nLinked List:")
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next

            print("NULL")


def linked_list_menu():
    linked_list = LinkedList()

    while True:
        print("\n================================")
        print("          LINKED LIST")
        print("================================")
        print("[1] Insert Element")
        print("[2] Delete Element")
        print("[3] Display Linked List")
        print("[4] Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            letter = input("Enter a letter: ").upper()

            if len(letter) == 1 and letter.isalpha():
                linked_list.insert(letter)
            else:
                print("Please enter only one letter.")

        elif choice == "2":
            linked_list.delete()

        elif choice == "3":
            linked_list.display()

        elif choice == "4":
            print("Exiting Linked List Program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    linked_list_menu()
