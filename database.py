import sqlite3

db = sqlite3.connect("expenses.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT
)
""")

db.commit()


def add_expense(amount, category, description, expense_date):
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (amount, category, description, expense_date)
    )

    db.commit()


def get_expenses(category="All"):
    if category == "All":
        cursor.execute("SELECT * FROM expenses")
    else:
        cursor.execute(
            "SELECT * FROM expenses WHERE category = ?",
            (category,)
        )

    return cursor.fetchall()


def delete_expense(expense_id):
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    db.commit()


def update_expense(
    expense_id,
    amount,
    category,
    description,
    expense_date
):
    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?, date = ?
        WHERE id = ?
    """, (
        amount,
        category,
        description,
        expense_date,
        expense_id
    ))

    db.commit()


def get_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    return total


def get_category_totals():
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    return cursor.fetchall()


def close_database():
    db.close()