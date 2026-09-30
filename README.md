## Expense Tracker

Expense Tracker is a simple Python desktop application that helps users manage their daily expenses. It allows users to add, view, edit, and delete expenses, calculate total spending, filter expenses by category, and view expenses using a simple chart.

## Features

-Add new expenses
-View all expenses
-Edit expenses
-Delete expenses
-Filter expenses by category
-Calculate total spending
-Display expenses using a bar chart
-Store expense data using SQLite
-Basic input validation and error handling

## Technologies Used

-Python
-Tkinter
-SQLite
-Matplotlib

## Project Structure

Expense-Tracker/
│
├── main.py
├── gui.py
├── database.py
├── expense.py
├── validation.py
├── reports.py
├── chart.py
├── requirements.txt
├── README.md
└── statement.md

The SQLite database file expenses.db is created automatically when the program is run.

## Installation

Install the required Python library using:

python3 -m pip install -r requirements.txt

## How to Run

Run the following command:

python3 main.py

## How to Use

1. Enter the expense amount.
2. Select a category.
3. Enter a description.
4. Enter the date.
5. Click Add Expense.
6. The expense will appear in the table.
7. Select an expense to edit or delete it.
8. Use the category filter to view specific expenses.
9. Click Show Chart to view expenses by category.
10. The total amount spent is displayed at the bottom.

## Database

SQLite is used to store expense information.

Each expense contains:

-Amount
-Category
-Description
-Date

The database is automatically created as expenses.db.

## Error Handling

The application checks for invalid amounts, amounts less than or equal to zero, and missing categories. It also displays a warning if the user tries to edit or delete an expense without selecting one.

## Testing

The main features tested include:

-Adding a valid expense
-Entering an invalid amount
-Editing an expense
-Deleting an expense
-Filtering expenses
-Calculating total spending
-Displaying the expense chart
-Saving and retrieving expenses from SQLite

## Future Improvements

-Monthly expense reports
-Budget tracking
-Income tracking
-Export expenses to CSV
-Search functionality
-Improved user interface
-More types of charts

## Conclusion

Expense Tracker provides a simple way to record and manage daily expenses. The project demonstrates the use of Python, Tkinter, SQLite, SQL queries, input validation, and basic data visualization.