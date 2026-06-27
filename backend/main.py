#expenses is a list containing dictionaries expense
# from csv_file import save_expenses, load_expenses
# from budget_file import save_budgets, load_budgets
import matplotlib.pyplot as plt # type: ignore

from backend.expense_db import (
    add_expenses,
    get_all_expenses,
    delete_expenses,
    update_expenses,
    get_expense_by_category,
    get_expense_by_merchant,
    get_sorted_by_amount,
    get_total_spending,
    get_category_totals,
    get_monthly_expenses,
    get_monthly_report,
    get_sorted_by_merchant,
    get_sorted_by_date,
    get_highest_expense_monthly,
    get_lowest_expense_monthly,
    get_highest_expense,
    get_lowest_expense,

)
from backend.budget_db import (
    get_budget,
    set_budget,
    check_budget,
)
# from models import Expense
from backend.db import init_db


def display_expense(expense):
    print("-----------------------")
    print("Expense",expense["id"])
    print("Merchant:", expense["merchant"])
    print("Amount: ₹", expense["amount"])
    print("Date:", expense["date"])
    print("Category:", expense["category"])

init_db()
# expenses=load_expenses()
# budgets = load_budgets()
# print(expenses)
# print(budgets)

from datetime import datetime  # noqa: E402

def get_valid_date():
    while True:
        date = input("Date (yyyy-mm-dd): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")

def get_valid_amount():
    while True:
        try:
            return float(input("Amount: "))
        except ValueError:
            print("Please enter a valid number.")

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
    print("17.Dashboard")
    print("18.Category Pie Chart")
    print("19.Monthly Trend")
    print("20.Category Bar Chart")
    print("21.Exit\n")

    choice=input("Choose: ")

    if choice=="1":

        merchant = input("Merchant: ")
        amount = get_valid_amount()
        date = get_valid_date()

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

        # expense = {
        #     "merchant": merchant,
        #     "amount": amount,
        #     "date": date,
        #     "category": category
        # }

        # expenses.append(expense)
        # save_expenses(expenses)
        # print("Expense Added!")
        add_expenses(merchant,amount,date,category)
        print("Expense Added!")

    elif choice=="2":
        print("\nExpenses:")
        
        expenses=get_all_expenses()
        for expense in expenses:
            display_expense(expense)
 

    elif choice=="3":
        total=get_total_spending()
        # expenses=get_all_expense()
        # for expense in expenses:
        #     total+=expense["amount"]
        print("Total Spending is: ₹",total)
    elif choice=="4":
        expenses=get_all_expenses()

        if len(expenses)==0:
            print("No expense to delete.")
        else:
            # print("\nExpenses:")
            # for i,expense in enumerate(expenses,start=1):
            #     print(f"{i}. {expense["merchant"]} - ₹{expense["amount"]}")
            # delete_num=int(input("Enter expense number to be deleted: "))
            # if 1<= delete_num<=len(expenses):
            #     expenses.pop(delete_num-1)
            #     save_expenses(expenses)
            #     print("Expense Deleted!")
            # else:
            #     print("Inalid Expense Number.")
            print("\nExpenses:")
            for expense in expenses:
                display_expense(expense)

            delete_index=int(input("Enter Expense ID to be deleted: "))
            confirm=input("Are you sure? (Y/N): ").strip().upper()
            if confirm.upper() == "Y":
                delete_expenses(delete_index)
                print("Expense Deleted!")
            elif confirm.upper() == "N":
                print("Deletion Cancelled.")
            else:
                print("Invalid Choice.")

    elif choice=="5":
        found=False
        select_cat=input("Enter the category to search: ")
        expenses=get_expense_by_category(select_cat)
        if len(expenses)==0:
            print("No such merchant found.")
        else:
            for expense in expenses:
                display_expense(expense)
                # print("--------------------")
                # print("Merchant: ",expense["merchant"])
                # print("Amount: ₹",expense["amount"])
                # print("Date(yyyy-mm-dd): ",expense["date"])
            #     found=True
            # if not found:
            #     print("No expense for this category was found")
    elif choice=="6":
        
        select_merch=input("Enter the merchant to search: ")

        expenses=get_expense_by_merchant(select_merch)

        if len(expenses)==0:
            print("No such merchant found.")

        else:
            for expense in expenses:
                display_expense(expense)
                # print("--------------------")
                # print("Category: ",expense["category"])
                # print("Amount: ₹",expense["amount"])
                # print("Date(yyyy-mm-dd)): ",expense["date"])
        #         found=True
        # if not found:
        #         print("No expense for this category was found")
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
        # category_total={}
        # for expense in expenses:

        #     category=expense["category"]
        #     amount=expense["amount"]

        #     if category not in category_total:
        #         category_total[category]=0;
        #     category_total[category]+=amount
        # print("\nCategory-wise Expenses:")
        # for category in category_total:
        #     print("--------------------")
        #     print(category,": ₹",category_total[category])
        category_total=get_category_totals()

        for category, amount in category_total:
            print(category,": ₹",amount)


    elif choice=="8":
        # if len(expenses)==0:
        #     print("No expense to delete.")
        # else:
        #     print("\nExpenses:")
        #     for i, expense in enumerate(expenses, start=1):
        #         print("--------------------")
        #         print("Expense", i)
        #         print("Merchant:", expense["merchant"])
        #         print("Amount: ₹", expense["amount"])
        #         print("Date:", expense["date"])
        #         print("Category:", expense["category"])
        #     print("\n--------------------\n")
        #     edit_num=int(input("Enter index of to be edited Expense: "))
        #     if 1<= edit_num<=len(expenses):
        #         edit_index=edit_num-1
        #         New_merch=input("Eneter the new merchant: ")
        #         New_cat=input("Eneter the new category: ")
        #         New_amt=input("Enter the new amount: ")
        #         New_date=input("Eneter the new date: ")
        #         expenses[edit_index]={
        #             "merchant":New_merch,
        #             "amount":float(New_amt),
        #             "date":New_date,
        #             "category":New_cat
        #         }
        #         save_expenses(expenses)
        #     else:
        #         print("Invalid index entered")
        expenses=get_all_expenses()

        if len(expenses)==0:
            print("No expense to update.")

        else:
            for expense in expenses:
                display_expense(expense)

            print("\n--------------------\n")
            edit_idx=int(input("Enter Expense ID to edit: "))

            New_merch=input("Eneter the new merchant: ")
            New_cat=input("Eneter the new category: ")
            New_amt=float(input("Enter the new amount: "))
            New_date=input("Eneter the new date: ")

            update_expenses(edit_idx,New_merch,New_amt,New_date,New_cat)

            print("Expense was updted!")
    elif choice=="9":
        # monthly_total={}
        # for expense in expenses:
        #     date=expense["date"]
        #     parts=date.split("-")
        #     month_date=parts[0]+"-"+parts[1]
        #     month=month_date
        #     amount=expense["amount"]
        #     if month not in monthly_total:
        #         monthly_total[month]=0
        #     monthly_total[month]+=amount
        # print("\nMonth-wise Expenses:")
        # for dates in monthly_total:
        #     print("--------------------")
        #     print(dates,": ₹",monthly_total[dates])
        monthly_total=get_monthly_expenses()
        print("\nMonthly-wise Expense:")
        for month,amount in monthly_total:
            print("--------------------")
            print(month,": ₹",amount)

    elif choice=="10":
        # sorted_expenses=sorted(expenses, key=lambda expense:expense["amount"])
        expenses=get_sorted_by_amount()

        print("\nExpenses Sorted by Amount:")

        for expense in expenses:
            display_expense(expense)
        # for expense in sorted_expenses:
        #     print("--------------------")
        #     print("Merchant:", expense["merchant"])
        #     print("Amount: ₹", expense["amount"])
        #     print("Date:", expense["date"])
        #     print("Category:", expense["category"])
    elif choice=="11":
        # sorted_expenses=sorted(expenses, key=lambda expense:expense["merchant"])
        expenses=get_sorted_by_merchant()
        
        print("\nExpenses Sorted by Merchant:")

        for expense in expenses:
            display_expense(expense)
        # for expense in sorted_expenses:
        #     print("--------------------")
        #     print("Merchant:", expense["merchant"])
        #     print("Amount: ₹", expense["amount"])
        #     print("Date:", expense["date"])
        #     print("Category:", expense["category"])
    elif choice=="12":
        # sorted_expenses=sorted(expenses, key=lambda expense:expense["date"])
        expenses=get_sorted_by_date()
        
        print("\nExpenses Sorted by Date:")

        for expense in expenses:
            display_expense(expense)
        # for expense in sorted_expenses:
        #     print("--------------------")
        #     print("Merchant:", expense["merchant"])
        #     print("Amount: ₹", expense["amount"])
        #     print("Date:", expense["date"])
        #     print("Category:", expense["category"])
    elif choice=="13":
        category=input("Enter the category: ")
        budget=float(input("Enter the budget of the above category: ₹"))
        # budgets[category]=budget
        # save_budgets(budgets)
        # print("Budget Saved!")

        set_budget(category,budget)

        print("Buget is set!")

    elif choice=="14":
        budgets=get_budget()

        print("\nBudgets:")

        for category,budget in budgets:
            print(category,": ₹",budget)

    elif choice=="15":

        # category_total={}
        # for expense in expenses:

        #     category=expense["category"]
        #     amount=expense["amount"]

        #     if category not in category_total:
        #         category_total[category]=0;
        #     category_total[category]+=amount
        # for category in budgets:
        #     if category_total[category]>budgets[category]:
        #         print("X Budget Exceeded")
        #     else:
        #         print("Within Budget")
        results=check_budget()
         
        for category,spend,budget in results:
            if spend>budget:
                print(category,"- Exceeded ❌")

            else:
                print(category,"- Within Budget ✅")

    elif choice=="16":
        # monthly_expenses=[]
        # month_rep=input("Enter the month you want the report for(mm.yy): ")
        # month_names = {
        #     "01": "January",
        #     "02": "February",
        #     "03": "March",
        #     "04": "April",
        #     "05": "May",
        #     "06": "June",
        #     "07": "July",
        #     "08": "August",
        #     "09": "September",
        #     "10": "October",
        #     "11": "November",
        #     "12": "December"
        # }
        # parts = month_rep.split(".")
        # month_num = parts[0]
        # year = "20" + parts[1]

        # month_name = month_names[month_num]

        # print("\n==========", month_name, year, "==========")
        # for expense in expenses:
        #     date=expense["date"]
        #     parts=date.split(".")
        #     month_date=parts[1]+"."+parts[2]
        #     month=month_date
        #     if month==month_rep:
        #         monthly_expenses.append(expense)
        # monthly_cat={}
        # max_spend=0
        # max_spend_merch=""
        # for expense in monthly_expenses:

        #     category=expense["category"]
        #     amount=expense["amount"]

        #     if category not in monthly_cat:
        #         monthly_cat[category]=0;
        #     monthly_cat[category]+=amount
        # total=0
        # for expense in monthly_expenses:
        #     total+=expense["amount"]
        # print("\nTotal Spending this month: ₹",total)
        # print("\nCategory Breakdown:")
        # for category in monthly_cat:
        #     print("--------------------")
        #     print(category,": ₹",monthly_cat[category])
        # min_spend=monthly_expenses[0]["amount"]
        # min_spend_mercht=""
        # for expense in monthly_expenses:
        #     if expense["amount"]>=max_spend:
        #         max_spend=expense["amount"]
        #         max_spend_merch=expense["merchant"]
        #     elif expense["amount"]<=min_spend:
        #         min_spend=expense["amount"]
        #         min_spend_merch=expense["merchant"]
        # print("\nHighest Expense this month:")
        # print(max_spend_merch,"- ₹",max_spend)
        # print("\nLowest Expense this month:")
        # print(min_spend_merch,"- ₹",min_spend)
        # print("\nNumber of transactions:")
        # print(len(monthly_expenses))
        month_rep=input("Enter the month you want the report for(yyyy-mm): ")

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
        parts = month_rep.split("-")
        month_num = parts[1]
        year = parts[0]
        month_name = month_names[month_num]

        monthly_expenses=get_monthly_report(month_rep)

        print("\n==========", month_name, year, "==========")
        
        monthly_expenses = get_monthly_report(month_rep)

        if len(monthly_expenses) == 0:
            print("No expenses found for this month.")

        else:

            print("\nMonthly Report:", month_rep)

            total = 0

            for expense in monthly_expenses:
                display_expense(expense)
                total += expense["amount"]

            print("--------------------")
            print("Total Spending: ₹", total)
            print("Number of Transactions:", len(monthly_expenses))

            category_total = {}

            for expense in monthly_expenses:
                category = expense["category"]

                if category not in category_total:
                    category_total[category] = 0

                category_total[category] += expense["amount"]
        
            print("\nCategory Breakdown:")

            for category in category_total:
                print(category, ": ₹", category_total[category])
        
            highest = get_highest_expense_monthly(month_rep)
            lowest = get_lowest_expense_monthly(month_rep)

            print("\nHighest Expense:")
            print(highest["merchant"], "- ₹", highest["amount"])

            print("\nLowest Expense:")
            print(lowest["merchant"], "- ₹", lowest["amount"])
            print("\nAverage Expense: ₹",(total/len(monthly_expenses)))
    elif choice=="17":
        expenses=get_all_expenses()

        print("\n============ Dashboard ============")

        print("Total Expenses: ",len(expenses))

        total=get_total_spending()
        print("Total Spendingg: ",total)

        if len(expenses)>0:
            avg_spend=total/len(expenses)
        else:
            avg_spend=0
        print("Average Transaction: ",round(avg_spend,2))

        cat_total=get_category_totals()
        print("Categories Used: ",len(cat_total))

        highest_spend=get_highest_expense()
        print("Highest expense Ever: ",highest_spend["merchant"], "- ₹", highest_spend["amount"])

        lowest_spend=get_lowest_expense()
        print("Lowest expense Ever: ₹",lowest_spend["merchant"], "- ₹", lowest_spend["amount"])

        cat_total=get_category_totals()
        print("Categories Used: ",len(cat_total))

    elif choice == "18":

        data = get_category_totals()

        categories = []
        amounts = []

        for category, amount in data:
            categories.append(category)
            amounts.append(amount)

        plt.figure(figsize=(7,7))

        plt.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%"
        )

        plt.title("Expense Distribution by Category")
        plt.show()

    elif choice == "19":

        data = get_monthly_expenses()

        months = []
        amounts = []

        for month, amount in data:
            months.append(month)
            amounts.append(amount)

        plt.figure(figsize=(8,5))

        plt.plot(months, amounts, marker="o")

        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.title("Monthly Spending Trend")

        plt.grid()
        plt.show()

    elif choice == "20":

        data = get_category_totals()

        categories = []
        amounts = []

        for category, amount in data:
            categories.append(category)
            amounts.append(amount)

        plt.figure(figsize=(8,5))

        plt.bar(categories, amounts)

        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expenses by Category")

        plt.show()

    elif choice=="21":
        break
