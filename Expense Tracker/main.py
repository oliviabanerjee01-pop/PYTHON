Expenses = []
def add_expenses():
    while True:
        amount = float(input("enter your amount: "))
        category = input ("enter category like rent travel or food: ")
    
        expense = {"amount":amount,"category":category}

        Expenses.append(expense)
        print("Expense added!")

        another = input("add another? (yes/no): ")
        if another.lower()=="no":
            break

    

def view_all():
    for expense in Expenses:
        print(expense)

    

def view_by_category():
    view=input("what category you wanna view: ")
    for expense in Expenses:
        if expense["category"].lower()== view.lower():
            print(expense)

    

def total_spent():
    total1 = 0
    for expense in Expenses:
        total1= total1 +expense["amount"]
    print("the total is:", total1)
    

def total_by_category():
    total2 =0
    category = input("what category?: ")
    for expense in Expenses:
        if expense["category"].lower()==category.lower():
            total2 = total2 + expense["amount"]
    print(total2)
    

def delete_expenses():
    for i in range(len(Expenses)):
        print(i, Expenses[i])

    index = int(input("Enter number: "))
    Expenses.pop(index)
    print("Expense deleted!")

print("welcome! Let's add your expenses first")
add_expenses()

while True:
    print("1. Add expense")
    print("2. View all")
    print("3. View by category")
    print("4. Total spent")
    print("5. Total by category")
    print("6. Delete expense")
    print("7. exit")

    choice = input("Enter your choice: ")

    if choice =="1":
        add_expenses()
    elif choice =="2":
        view_all()
    elif choice =="3":
        view_by_category()
    elif choice =="4":
        total_spent()
    elif choice =="5":
        total_by_category()
    elif choice =="6":
        delete_expenses()
    elif choice=="7":
        break






   
