import matplotlib.pyplot as plt
from database import get_category_totals


def show_expense_chart():
    rows = get_category_totals()

    if not rows:
        return False

    categories = []
    amounts = []

    for row in rows:
        categories.append(row[0])
        amounts.append(row[1])

    plt.figure(figsize=(7, 5))

    plt.bar(categories, amounts)

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()

    return True