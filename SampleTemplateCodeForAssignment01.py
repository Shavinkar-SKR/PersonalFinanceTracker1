import json

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    pass

def save_transactions():
    pass

# Feature implementations
def add_transaction():
    pass

def view_transactions():
    pass

def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating
    pass

def delete_transaction():
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    pass

def display_summary():
    # Placeholder for summary display logic
    pass

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
