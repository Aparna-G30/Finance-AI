#expenses is a list containing dictionaries expense
expenses=[]

while True:
    print("\n1.Add Expenses")
    print("2.View Expenses")
    print("3.Total Spending")
    print("4.Delete an Expense")
    print("5.Search by Category")
    print("6.Sreach by Merchant")
    print("7.Exit\n")

    choice=input("Choose: ")

    if choice=="1":

        merchant = input("Merchant: ")
        amount = float(input("Amount: "))
        date = input("Date(dd.mm.yy): ")

        print("\nChoose Category:")
        print("1. Food")
        print("2. Shopping")
        print("3. Travel")
        print("4. Bills")
        print("5. Entertainment")

        category_choice = input("Enter choice: ")

        if category_choice == "1":
            category = "Food"
        elif category_choice == "2":
            category = "Shopping"
        elif category_choice == "3":
            category = "Travel"
        elif category_choice == "4":
            category = "Bills"
        elif category_choice == "5":
            category = "Entertainment"
        else:
            category = "Other"

        expense = {
            "merchant": merchant,
            "amount": amount,
            "date": date,
            "category": category
        }

        expenses.append(expense)
        print("Expense Added!")

    elif choice=="2":
        print("\nExpenses:")
        for i, expense in enumerate(expenses, start=1):
            print("--------------------")
            print("Expense", i)
            print("Merchant:", expense["merchant"])
            print("Amount: ₹", expense["amount"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])

    elif choice=="3":
        total=0
        for expense in expenses:
            total+=expense["amount"]
        print("Total Spending is: ₹",total)
    elif choice=="4":
        if len(expenses)==0:
            print("No expense to delete.")
        else:
            print("\nExpenses:")
            for i,expense in enumerate(expenses,start=1):
                print(f"{i}. {expense["merchant"]} - ₹{expense["amount"]}")
            delete_num=int(input("Enter expense number to be deleted: "))
            if 1<= delete_num<=len(expenses):
                expenses.pop(delete_num-1)
                print("Expense Deleted!")
            else:
                print("Inalid Expense Number.")
    elif choice=="5":
        found=False
        select_cat=input("Enter the category to search: ")
        for expense in expenses:
            if expense["category"].lower()==select_cat.lower():
                print("--------------------")
                print("Merchant: ",expense["merchant"])
                print("Amount: ₹",expense["amount"])
                print("Date(dd.mm.yy): ",expense["date"])
                found=True
            if not found:
                print("No expense for this category was found")
    elif choice=="6":
        found=False
        select_merch=input("Enter the merchant to search: ")
        for expense in expenses:
            if expense["merchant"].lower()==select_merch.lower():
                print("--------------------")
                print("Category: ",expense["Category"])
                print("Amount: ₹",expense["amount"])
                print("Date(dd.mm.yy): ",expense["date"])
                found=True
        if not found:
                print("No expense for this category was found")
    elif choice=="7":
        break
