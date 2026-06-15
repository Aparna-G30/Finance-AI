import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUDGETS_FILE = os.path.join(BASE_DIR, "budgets.csv")

def save_budgets(budgets):

    with open(BUDGETS_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["category", "budget"])

        for category in budgets:

            writer.writerow([
                category,
                budgets[category]
            ])
def load_budgets():
    import os
    print("Loading budgets from:", os.path.abspath("budgets.csv"))

    loaded_budgets = {}

    try:

        with open(BUDGETS_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                loaded_budgets[row["category"]] = float(row["budget"])

    except FileNotFoundError:
        pass

    return loaded_budgets