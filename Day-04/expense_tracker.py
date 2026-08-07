import csv
import os

FILE = "expenses.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def get_amount():
    while True:
        try:
            return float(input("Enter Amount: "))
        except ValueError:
            print("Please enter a valid amount.")


def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = get_amount()
    note = input("Enter Note: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    print("Expense Added Successfully!\n")


def view_expenses():
    total = 0

    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)

        for date, category, amount, note in reader:
            amount = float(amount)
            total += amount
            print(date, "|", category, "|", amount, "|", note)

    print("Total Amount =", total)


def category_summary():
    total = {}

    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)

        for date, category, amount, note in reader:
            total[category] = total.get(category, 0) + float(amount)

    print("\nCategory Summary")
    for category, amount in total.items():
        print(category, "=", amount)


def main():
    init_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")


main()
