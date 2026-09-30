import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from expense import (
    save_expense,
    load_expenses,
    remove_expense,
    edit_expense
)

from validation import (
    valid_amount,
    valid_category
)

from reports import total_spending
from chart import show_expense_chart
from database import close_database


CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Bills",
    "Entertainment",
    "Other"
]


def create_app():

    root = tk.Tk()

    root.title("Expense Tracker")
    root.geometry("850x600")


    def add():

        if not valid_amount(amount.get()):
            messagebox.showerror(
                "Error",
                "Enter a valid amount"
            )
            return

        if not valid_category(category.get()):
            messagebox.showerror(
                "Error",
                "Select a category"
            )
            return

        save_expense(
            float(amount.get()),
            category.get(),
            description.get(),
            expense_date.get()
        )

        amount.delete(0, tk.END)
        description.delete(0, tk.END)

        show_expenses()


    def show_expenses():

        for item in table.get_children():
            table.delete(item)

        rows = load_expenses(
            filter_category.get()
        )

        for row in rows:

            table.insert(
                "",
                tk.END,
                iid=str(row[0]),
                values=row[1:]
            )

        update_total()


    def delete_selected():

        selected = table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select an expense first"
            )
            return

        remove_expense(selected[0])

        show_expenses()


    def edit_selected():

        selected = table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select an expense first"
            )
            return

        expense_id = selected[0]

        item = table.item(selected[0])

        data = item["values"]


        edit_window = tk.Toplevel(root)

        edit_window.title("Edit Expense")

        edit_window.geometry("400x300")


        tk.Label(
            edit_window,
            text="Amount"
        ).pack(pady=5)


        edit_amount = tk.Entry(
            edit_window,
            bg="white",
            fg="black",
            insertbackground="black"
        )

        edit_amount.insert(
            0,
            data[0]
        )

        edit_amount.pack()


        tk.Label(
            edit_window,
            text="Category"
        ).pack(pady=5)


        edit_category = ttk.Combobox(
            edit_window,
            values=CATEGORIES,
            state="readonly"
        )

        edit_category.set(
            data[1]
        )

        edit_category.pack()


        tk.Label(
            edit_window,
            text="Description"
        ).pack(pady=5)


        edit_description = tk.Entry(
            edit_window,
            bg="white",
            fg="black",
            insertbackground="black"
        )

        edit_description.insert(
            0,
            data[2]
        )

        edit_description.pack()


        tk.Label(
            edit_window,
            text="Date"
        ).pack(pady=5)


        edit_date = tk.Entry(
            edit_window,
            bg="white",
            fg="black",
            insertbackground="black"
        )

        edit_date.insert(
            0,
            data[3]
        )

        edit_date.pack()


        def save_changes():

            if not valid_amount(
                edit_amount.get()
            ):
                messagebox.showerror(
                    "Error",
                    "Enter a valid amount"
                )
                return

            if not valid_category(
                edit_category.get()
            ):
                messagebox.showerror(
                    "Error",
                    "Select a category"
                )
                return

            edit_expense(
                expense_id,
                float(edit_amount.get()),
                edit_category.get(),
                edit_description.get(),
                edit_date.get()
            )

            edit_window.destroy()

            show_expenses()


        tk.Button(
            edit_window,
            text="Save Changes",
            command=save_changes
        ).pack(pady=15)


    def update_total():

        total = total_spending()

        total_label.config(
            text="Total Spent: ₹"
            + str(round(total, 2))
        )


    def show_chart():

        result = show_expense_chart()

        if not result:

            messagebox.showinfo(
                "Chart",
                "Add some expenses first"
            )


    title = tk.Label(
        root,
        text="Expense Tracker",
        font=("Arial", 22, "bold")
    )

    title.pack(pady=15)


    input_frame = tk.Frame(root)

    input_frame.pack(pady=5)


    tk.Label(
        input_frame,
        text="Amount"
    ).grid(
        row=0,
        column=0,
        padx=5
    )


    amount = tk.Entry(
        input_frame,
        bg="white",
        fg="black",
        insertbackground="black"
    )

    amount.grid(
        row=1,
        column=0,
        padx=5
    )


    tk.Label(
        input_frame,
        text="Category"
    ).grid(
        row=0,
        column=1,
        padx=5
    )


    category = ttk.Combobox(
        input_frame,
        values=CATEGORIES,
        state="readonly"
    )

    category.grid(
        row=1,
        column=1,
        padx=5
    )


    tk.Label(
        input_frame,
        text="Description"
    ).grid(
        row=0,
        column=2,
        padx=5
    )


    description = tk.Entry(
        input_frame,
        bg="white",
        fg="black",
        insertbackground="black"
    )

    description.grid(
        row=1,
        column=2,
        padx=5
    )


    tk.Label(
        input_frame,
        text="Date"
    ).grid(
        row=0,
        column=3,
        padx=5
    )


    expense_date = tk.Entry(
        input_frame,
        bg="white",
        fg="black",
        insertbackground="black"
    )

    expense_date.insert(
        0,
        str(date.today())
    )

    expense_date.grid(
        row=1,
        column=3,
        padx=5
    )


    tk.Button(
        input_frame,
        text="Add Expense",
        command=add
    ).grid(
        row=1,
        column=4,
        padx=10
    )


    filter_frame = tk.Frame(root)

    filter_frame.pack(pady=10)


    tk.Label(
        filter_frame,
        text="Filter by Category:"
    ).pack(
        side="left",
        padx=5
    )


    filter_category = ttk.Combobox(
        filter_frame,
        values=["All"] + CATEGORIES,
        state="readonly",
        width=18
    )

    filter_category.set("All")

    filter_category.pack(
        side="left"
    )


    tk.Button(
        filter_frame,
        text="Filter",
        command=show_expenses
    ).pack(
        side="left",
        padx=5
    )


    table_frame = tk.Frame(root)

    table_frame.pack(
        pady=15,
        fill="both",
        expand=True
    )


    columns = (
        "Amount",
        "Category",
        "Description",
        "Date"
    )


    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


    for column in columns:

        table.heading(
            column,
            text=column
        )


    table.column(
        "Amount",
        width=120
    )

    table.column(
        "Category",
        width=150
    )

    table.column(
        "Description",
        width=300
    )

    table.column(
        "Date",
        width=150
    )


    table.pack(
        fill="both",
        expand=True
    )


    button_frame = tk.Frame(root)

    button_frame.pack(
        pady=5
    )


    tk.Button(
        button_frame,
        text="Delete Selected",
        command=delete_selected
    ).pack(
        side="left",
        padx=5
    )


    tk.Button(
        button_frame,
        text="Edit Selected",
        command=edit_selected
    ).pack(
        side="left",
        padx=5
    )


    tk.Button(
        button_frame,
        text="Show Chart",
        command=show_chart
    ).pack(
        side="left",
        padx=5
    )


    total_label = tk.Label(
        root,
        text="Total Spent: ₹0",
        font=("Arial", 15, "bold")
    )

    total_label.pack(
        pady=10
    )


    show_expenses()


    return root, close_database