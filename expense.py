from database import (
    add_expense,
    get_expenses,
    delete_expense,
    update_expense
)


def save_expense(
    amount,
    category,
    description,
    expense_date
):
    add_expense(
        amount,
        category,
        description,
        expense_date
    )


def load_expenses(category="All"):
    return get_expenses(category)


def remove_expense(expense_id):
    delete_expense(expense_id)


def edit_expense(
    expense_id,
    amount,
    category,
    description,
    expense_date
):
    update_expense(
        expense_id,
        amount,
        category,
        description,
        expense_date
    )