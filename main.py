#expenses is a list containing dictionaries expense
from csv_file import save_expenses, load_expenses
from budget_file import save_budgets, load_budgets

def dispaly_expense(expense,index=None):
    print("-----------------------")
    if index is not None:
        print("Expense",index)
    print("Merchant:", expense["merchant"])
    print("Amount: ₹", expense["amount"])
    print("Date:", expense["date"])
    print("Category:", expense["category"])


expenses=load_expenses()
budgets = load_budgets()
# print(expenses)
# print(budgets)

while True:
    print("\n1.Add Expenses")
    print("2.View Expenses")
    print("3.Total Spending")
    print("4.Delete an Expense")
    print("5.Search by Category")
    print("6.Sreach by Merchant")
    print("7.Get total Category-wise")
    print("8.Edit an Expense")
    print("9.Monthl-Wise Expense")
    print("10.Sort by Amount")
    print("11.Sort by Merchant")
    print("12.Sort by Date")
    print("13.Set Budget")
    print("14.View Budget")
    print("15.Check Budget")
    print("16.Get Monthly reports")
    print("17.Exit\n")

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
        save_expenses(expenses)
        print("Expense Added!")

    elif choice=="2":
        print("\nExpenses:")
        for i, expense in enumerate(expenses, start=1):
            dispaly_expense(expense,i)

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
                save_expenses(expenses)
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
        # categories=set()
        # for expense in expenses:
        #     categories.add(expense["category"])
        # for category in categories:
        #     total=0
        #     for expense in expenses:
        #         if expense["category"].lower()==category.lower():
        #             total+=expense["amount"]
        #     print(category,": ₹",total)
        category_total={}
        for expense in expenses:

            category=expense["category"]
            amount=expense["amount"]

            if category not in category_total:
                category_total[category]=0;
            category_total[category]+=amount
        print("\nCategory-wise Expenses:")
        for category in category_total:
            print("--------------------")
            print(category,": ₹",category_total[category])
    elif choice=="8":
        if len(expenses)==0:
            print("No expense to delete.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print("--------------------")
                print("Expense", i)
                print("Merchant:", expense["merchant"])
                print("Amount: ₹", expense["amount"])
                print("Date:", expense["date"])
                print("Category:", expense["category"])
            print("\n--------------------\n")
            edit_num=int(input("Enter index of to be edited Expense: "))
            if 1<= edit_num<=len(expenses):
                edit_index=edit_num-1
                New_merch=input("Eneter the new merchant: ")
                New_cat=input("Eneter the new category: ")
                New_amt=input("Enter the new amount: ")
                New_date=input("Eneter the new date: ")
                expenses[edit_index]={
                    "merchant":New_merch,
                    "amount":float(New_amt),
                    "date":New_date,
                    "category":New_cat
                }
                save_expenses(expenses)
            else:
                print("Invalid index entered")
    elif choice=="9":
        monthly_total={}
        for expense in expenses:
            date=expense["date"]
            parts=date.split(".")
            month_date=parts[1]+"."+parts[2]
            month=month_date
            amount=expense["amount"]
            if month not in monthly_total:
                monthly_total[month]=0
            monthly_total[month]+=amount
        print("\nMonth-wise Expenses:")
        for dates in monthly_total:
            print("--------------------")
            print(dates,": ₹",monthly_total[dates])
    elif choice=="10":
        sorted_expenses=sorted(expenses, key=lambda expense:expense["amount"])
        print("\nExpenses Sorted by Amount:")

        for expense in sorted_expenses:
            print("--------------------")
            print("Merchant:", expense["merchant"])
            print("Amount: ₹", expense["amount"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])
    elif choice=="11":
        sorted_expenses=sorted(expenses, key=lambda expense:expense["merchant"])
        print("\nExpenses Sorted by Merchant:")

        for expense in sorted_expenses:
            print("--------------------")
            print("Merchant:", expense["merchant"])
            print("Amount: ₹", expense["amount"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])
    elif choice=="12":
        sorted_expenses=sorted(expenses, key=lambda expense:expense["date"])
        print("\nExpenses Sorted by Date:")

        for expense in sorted_expenses:
            print("--------------------")
            print("Merchant:", expense["merchant"])
            print("Amount: ₹", expense["amount"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])
    elif choice=="13":
        category=input("Enter the category: ")
        budget=input("Enter the budget of the above category: ₹")
        budgets[category]=budget
        save_budgets(budgets)
        print("Budget Saved!")
    elif choice=="14":
        for category in budgets:
            print(category,": ₹",budgets[category])
    elif choice=="15":
        for category in budgets:
            if category_total[category]>budgets[category]:
                print("X Budget Exceeded")
            else:
                print("Within Budget")
    elif choice=="16":
        monthly_expenses=[]
        month_rep=input("Enter the month you want the report for(mm.yy): ")
        month_names = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        parts = month_rep.split(".")
        month_num = parts[0]
        year = "20" + parts[1]

        month_name = month_names[month_num]

        print("\n==========", month_name, year, "==========")
        for expense in expenses:
            date=expense["date"]
            parts=date.split(".")
            month_date=parts[1]+"."+parts[2]
            month=month_date
            if month==month_rep:
                monthly_expenses.append(expense)
        monthly_cat={}
        max_spend=0
        max_spend_merch=""
        for expense in monthly_expenses:

            category=expense["category"]
            amount=expense["amount"]

            if category not in monthly_cat:
                monthly_cat[category]=0;
            monthly_cat[category]+=amount
        total=0
        for expense in monthly_expenses:
            total+=expense["amount"]
        print("\nTotal Spending this month: ₹",total)
        print("\nCategory Breakdown:")
        for category in monthly_cat:
            print("--------------------")
            print(category,": ₹",monthly_cat[category])
        min_spend=monthly_expenses[0]["amount"]
        min_spend_mercht=""
        for expense in monthly_expenses:
            if expense["amount"]>=max_spend:
                max_spend=expense["amount"]
                max_spend_merch=expense["merchant"]
            elif expense["amount"]<=min_spend:
                min_spend=expense["amount"]
                min_spend_merch=expense["merchant"]
        print("\nHighest Expense this month:")
        print(max_spend_merch,"- ₹",max_spend)
        print("\nLowest Expense this month:")
        print(min_spend_merch,"- ₹",min_spend)
        print("\nNumber of transactions:")
        print(len(monthly_expenses))
    elif choice=="17":
        break
