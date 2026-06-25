from fastapi import FastAPI
from .expense_db import (
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
    get_expense_by_id,
    search_expenses,
    get_expense_by_category_month,

)
from .budget_db import (
    get_budget,
    set_budget,
    check_budget,
)

from .models import Expense
from .models import ExpenseResponse
from typing import List
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return{"message":"Finance Ai"}

@app.get("/about")
def about():
    return{"project": "Finance AI"}

# @app.get("/expense/{expense_id}")
# def get_expense(expense_id:int):
#     return{"expense_id": expense_id}

@app.get("/hello/{name}")
def greet(name:str):
    return{"message": f"Hello {name}"}

@app.get("/expenses/filter")
def get_expense_by_category_api(category:str):
    expense=get_expense_by_category(category)
    return expense

@app.get("/expenses/{expense_id}",tags=["Expenses"], response_model=ExpenseResponse)#
def get_expenses_by_id_api(expense_id:int):
    expense= get_expense_by_id(expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )
    return expense

@app.get("/expenses",tags=["Expenses"], response_model=List[ExpenseResponse])#
def get_all_expense_api():
    return get_all_expenses()

# @app.post("/expenses")
# def add_an_expense(merchant,amount,date,category):
#     add_expenses(merchant,amount,date,category)
#     return {
#         "message":"Expense was added successfully",
#          "expense": {
#             "merchant": merchant,
#             "amount": amount,
#             "date": date,
#             "category": category
#         }
#     }



@app.post("/expense",tags=["Expenses"],status_code=201)
def add_expense_api(expense:Expense):
    add_expenses(
        expense.merchant,
        expense.amount,
        expense.date,
        expense.category
    )
    return {"message":"Expense was added successfully"}

@app.put("/expenses/{expense_id}",tags=["Expenses"])
def edit_expense_api(expense_id:int ,expense:Expense):
    update_expenses(
        expense_id,
        expense.merchant,
        expense.amount,
        expense.date,
        expense.category
    )
    return {"message":"Expense updted successfully"}

@app.delete("/expenses/{expense_id}",tags=["Expenses"],status_code=204)
def delete_expense_api(expense_id:int):
    delete_expenses(expense_id)
    return {"message":"Expense deleted successfully"}



@app.get("/expenses/merchant")
def get_expense_by_merchant_api(merchant:str):
    expense=get_expense_by_merchant(merchant)
    return expense

@app.get("/expenses/search")
def search_expense_api(category:str=None,merchant:str=None):
    return search_expenses(category,merchant)

@app.get("/expenses/sort/amount", tags=["Expenses"])
def get_sorted_by_amount_api():
    expenses = get_sorted_by_amount()
    return expenses

@app.get("/expenses/sort/merchant", tags=["Expenses"])
def get_sorted_by_merchant_api():
    expenses = get_sorted_by_merchant()
    return expenses

@app.get("/expenses/sort/date", tags=["Expenses"])
def get_sorted_by_date_api():
    expenses = get_sorted_by_date()
    return expenses

@app.get("/reports/total",tags=["Reports"])
def get_total_spending_api():
    total=get_total_spending()
    return{"Total Spending":total}

@app.get("/reports/categories",tags=["Reports"])
def get_categoty_totals_api():
    return get_category_totals()

@app.get("/reports/highest",tags=["Reports"])
def get_highest_expense_api():
    highest=get_highest_expense()
    return{"Highest Expense":highest}

@app.get("/reports/lowest",tags=["Reports"])
def get_lowest_expense_api():
    lowest=get_lowest_expense()
    return{"Highest Expense":lowest}

@app.get("/reports/monthl-wise",tags=["Reports"])
def get_monthly_expenses_api():
    return get_monthly_expenses()

@app.get("/reports/monthly",tags=["Reports"])
def get_monthly_report_api(month_rep:str):
    monthly_expense=get_monthly_report(month_rep)
    
    total=0

    for expense in monthly_expense:
        total+=expense["amount"]

    if len(monthly_expense) > 0:
        average = int(total / len(monthly_expense))
    else:
        average = 0
    
    category_totals = {}

    for expense in monthly_expense:

        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]


    return{
        "month":month_rep,
        "total_spending":total,
        "number_of_transactions":len(monthly_expense),
        "average_expense":average,
        "category_breakdown": category_totals,
        "expenses": monthly_expense
    }

@app.get("/reports/monthly/highest", tags=["Reports"])
def highest_monthly_expense_api(month_rep: str):
    highest = get_highest_expense_monthly(month_rep)
    return highest

@app.get("/reports/monthly/lowest", tags=["Reports"])
def lowest_monthly_expense_api(month_rep: str):
    lowest = get_lowest_expense_monthly(month_rep)
    return lowest

@app.post("/budget", tags=["Budgets"])
def set_budget_api(category: str, amount: float):
    set_budget(category, amount)
    return {"message": "Budget set successfully"}

@app.get("/budget/{category}", tags=["Budgets"])
def get_budget_api(category: str):
    budget = get_budget(category)
    return budget

@app.get("/budget/check/{category}", tags=["Budgets"])
def check_budget_api(category: str):
    result = check_budget(category)
    return result

@app.get("/expenses/filter/month")
def get_expense_by_category_month_api(
    category:str,
    month_rep:str
):
    return get_expense_by_category_month(
        category,
        month_rep
    )