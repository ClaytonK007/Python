#
#   Create an expense tracker. Allow users to add expense, view total expenses by category,
#   display all transactions and save transactions to a file. 
#
expense = []

def add():
    try:
        date = input("Enter expense date (dd/mm/yyyy): ")
        category = input("Enter expense category (food, transport etc): ")
        price = float(input("Enter expense amount: "))
        expenses = {
            "date" : date,
            "category" : category,
            "price" : price
        }
        expense.append(expenses)
        print("Expense has been added.")
    except ValueError:
        print("Invalid price. Please enter numeric amount.")

def view():
    if not expense:
        print("No expenses recorded yet.")
        return
    
    print("List of all expenses:")
    print(f"-"*20)
    for exp in expense:
        print(f"{exp['date']}: {exp['category']} : ${exp['price']:.2f}")
    print(f"-"*20)

def save():
    with open("expenses.txt", 'w') as file:
        for exp in expense:
            file.write(f"{exp['date']}: {exp['category']} : ${exp['price']:.2f}\n")
        print("Expenses saved to file.")

while True:
    print("1. Add expense.\n2. View total expenses by category\n3. Save transactions to a file.\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        save()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose valid option.")