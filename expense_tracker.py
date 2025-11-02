# Personal Expense Tracker (CLI Version)

import json
import matplotlib.pyplot as plt
from datetime import datetime


class Expense_Tracker:
    def __init__(self):
        self.balance = 0
        self.Total_income = 0
        self.Total_expense = 0
        self.transactions = []
        self.load_data()

    def add_income(self):
        income = int(input("Add Income: "))
        source = input("Add Source: ")
        date = input("Add date (press Enter for today): ") or datetime.now().strftime("%Y-%m-%d")

        self.transactions.append({
            "Type": "Income",
            "Amount": income,
            "Description": source,
            "Date": date
        })

        self.balance += income
        self.Total_income += income
        self.save_data()

    def add_expense(self):
        expense = int(input("Add Expense: "))
        category = input("Add Category: ")
        date = input("Add date (press Enter for today): ") or datetime.now().strftime("%Y-%m-%d")

        self.transactions.append({
            "Type": "Expense",
            "Amount": expense,
            "Description": category,
            "Date": date
        })

        self.balance -= expense
        self.Total_expense += expense
        self.save_data()

    def view_summary(self):
        print("\n==== Summary ====")
        print(f"Total Income:   {self.Total_income} DA")
        print(f"Total Expenses: {self.Total_expense} DA")
        print(f"Balance:        {self.balance} DA")
        print("=================\n")

    def view_all_transactions(self):
        print("\n==== All Transactions ====")
        if not self.transactions:
            print("No transactions recorded yet.")
        else:
            for t in self.transactions:
                print(f"{t['Date']} | {t['Type']} | {t['Description']} | {t['Amount']} DA")
        print("==========================\n")

    def save_data(self):
        data = {
            "balance": self.balance,
            "Total_income": self.Total_income,
            "Total_expense": self.Total_expense,
            "transactions": self.transactions
        }
        with open("expense_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("expense_data.json", "r") as file:
                data = json.load(file)
                self.balance = data["balance"]
                self.Total_income = data["Total_income"]
                self.Total_expense = data["Total_expense"]
                self.transactions = data["transactions"]
        except FileNotFoundError:
            pass

    def view_expenses_by_category(self):
        category_totals = {}

        for t in self.transactions:
            if t["Type"] == "Expense":
                category = t["Description"]
                amount = t["Amount"]
                category_totals[category] = category_totals.get(category, 0) + amount

        if not category_totals:
            print("\nNo expenses recorded yet.\n")
            return

        print("\n==== Expenses by Category ====")
        for category, total in category_totals.items():
            print(f"{category}: {total} DA")
        print("==============================\n")

    def view_income_by_source(self):
        
        source_totals = {}
        for t in self.transactions:
            if t["Type"] == "Income":
                source = t["Description"]
                amount = t["Amount"]
                source_totals[source] = source_totals.get(source, 0) + amount
        if not source_totals:
            print("\n No Income recorded yet. \n")
            return
        print("\n==== Income by Source ====")
        for source , total in source_totals.items():
            print(f"{source}: {total} DA")
        print("==============================\n")


    def show_expense_chart(self):
        category_totals = {}

        for t in self.transactions:
            if t["Type"] == "Expense":
                category = t["Description"]
                amount = t["Amount"]
                category_totals[category] = category_totals.get(category, 0) + amount

        if not category_totals:
            print("\nNo expenses to display in chart.\n")
            return

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure(figsize=(6, 6))
        plt.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=90,
            shadow=True
        )
        plt.title("Expenses by Category")
        plt.show()


def main():
    tracker = Expense_Tracker()

    while True:
        print("************ Personal Expense Tracker ************")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Summary")
        print("4. View All Transactions")
        print("5. View Expenses by Category")
        print("6. View income by Source")
        print("7. Show Expense Chart")
        print("8. Exit")
        print("**************************************************")


        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.add_income()
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            tracker.view_all_transactions()
        elif choice == "5":
            tracker.view_expenses_by_category()
        elif choice == "6":
            tracker.view_income_by_source()
        elif choice == "7":
            tracker.show_expense_chart()
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")



main()
