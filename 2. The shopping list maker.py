'''
2. The Shopping List Maker

Objective:
The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way.

'''

class ShoppingList:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to the shopping list.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")

    def print_list(self):
        if self.items:
            print("Shopping List:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

def main():
    shopping_list = ShoppingList()
    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.add_item(item)
        elif choice == "2":
            item = input("Enter item to remove: ")
            shopping_list.remove_item(item)
        elif choice == "3":
            shopping_list.print_list()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()
              
            






