#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 06-02-2025
#    Capstone Project: Personal Finance Tracker

#-------------------------------------------------
print("Welcome to the Personal Finance Tracker!")

# Use a loop to repeatedly ask the user to enter expense description (string), category (string), and amount (float)
# Store each expense as a tuple: (description, amount). Use a dictionary to organize expenses by category.
# Handle exceptions for Non-numeric input for amounts,Empty inputs, and Unexpected errors

# Add a function to allow users to pick from menu options - Adding an expense, Viewing expenses, Viewing summary, Exit
# Add a function to add an expense that prompts the user for description, category, and amount.
def add_expense():
    while True:
        try:
            description = input("Enter expense description (or type 'exit' to go back to the menu): ")
            if description.lower() == 'exit':
                return None
            if not description.strip():
                raise ValueError("Description cannot be empty.")
            
            category = input("Enter expense category: ")
            if not category.strip():
                raise ValueError("Category cannot be empty.")
            
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a number greater than zero.")
            
            return (description, category, amount)
        
        except ValueError as ve:
            print(f"Invalid entry. Please enter a valid input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

 
# Define a function to add an expense to the expenses dictionary.
def add_expense_to_dict(expense, data):
    description, category, amount = expense
    if category not in data:
        data[category] = []
    data[category].append((description, amount))
    print(f"Expense added: {description} in category '{category}' for ${amount:.2f}")



# Define a function to display the menu options.
def display_menu():
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary by Category")
    print("4. Exit")



# Define a function view_expenses(data) that prints all categories and their expenses.
def view_expenses(data):
    print("\nView all expenses:")
    for category, items in data.items():
        print(f"\nCategory: {category}")
        for description, amount in items:
            print(f"  - {description}: ${amount:.2f}")
    total = sum(amount for items in data.values() for _, amount in items)
    print(f"Total Expenses: ${total:.2f}")



#Define a function view_summary(data) that shows the total amount spent per category.
def view_summary(data):
    print("\nView summary by category:")
    summary = {}
    for category, items in data.items():
        total_amount = sum(amount for _, amount in items)
        summary[category] = total_amount
        print(f"{category}: ${total_amount:.2f}")
    
    print("\nOverall Total Expenses: $", sum(summary.values()))



# Main loop to display the menu and handle user choices.
expenses = {}
print("Welcome to the Personal Finance Tracker!")
while True:
    display_menu()
    choice = input("Please enter your choice (1-4): ")
    
    if choice == '1':
        expense = add_expense()
        if expense is not None:
            add_expense_to_dict(expense, expenses)
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        view_summary(expenses)
    elif choice == '4':
        print("Exiting the Personal Finance Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")



