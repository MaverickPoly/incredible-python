import argparse
import sqlite3


DB = "expenses.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount FLOAT NOT NULL,
                description TEXT NOT NULL
            )
        """)


def add_expense(amount: float, description: str):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (amount, description) VALUES (?, ?)
        """, (amount, description,))

def get_expenses():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM expenses
        """)
        expenses = cursor.fetchall()

        expense_amount = 0
        for expense in expenses:
            expense_amount += expense[1]
        return expenses, expense_amount

def delete_expense(expense_id: int):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM expenses WHERE id=?
        """, (expense_id,))


def main():
    init_db()

    parser = argparse.ArgumentParser(description="Expense tracker")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("-a", "--amount", required=True, type=float, help="Expense amount")
    add_parser.add_argument("-d", "--description", required=True, help="Expense description")

    get_parser = subparsers.add_parser("get")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense id to delete")

    args = parser.parse_args()

    match args.command:
        case "add":
            add_expense(args.amount, args.description)
            print("Expense added successfully!")
        case "get":
            expenses, expense_amount = get_expenses()
            print(f"Total expense amount: {expense_amount}")
            for expense in expenses:
                print(f"{expense[0]}. {expense[2]} - {expense[1]}")
        case "delete":
            delete_expense(args.id)
            print("Expense deleted successfully!")

if __name__ == '__main__':
    main()
