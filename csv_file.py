import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSES_FILE = os.path.join(BASE_DIR, "expenses.csv")

def save_expenses(expenses):

    with open(EXPENSES_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["merchant", "amount", "date", "category"])

        for expense in expenses:

            writer.writerow([
                expense["merchant"],
                expense["amount"],
                expense["date"],
                expense["category"]
            ])
def load_expenses():
    import os
    print("Loading expenses from:", os.path.abspath("expenses.csv"))

    loaded_expenses = []

    try:

        with open(EXPENSES_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                expense = {
                    "merchant": row["merchant"],
                    "amount": float(row["amount"]),
                    "date": row["date"],
                    "category": row["category"]
                }

                loaded_expenses.append(expense)

    except FileNotFoundError:
        pass

    return loaded_expenses
