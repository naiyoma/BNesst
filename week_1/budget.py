import sqlite3
import tkinter as tk

def create_budget_db():
    connection = sqlite3.connect('budget.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY,
                        description TEXT,
                        amount REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        description TEXT,
                        amount REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS budget_goals (
                        id INTEGER PRIMARY KEY,
                        description TEXT,
                        amount REAL,
                        date DATE)''')
    connection.commit()
    connection.close()

create_budget_db()


def on_submit():
    income = income_entry.get()
    expense = expense_entry.get()
    budget_goal = budget_goal_entry.get()
    conn = sqlite3.connect("budget.db")
    c = conn.cursor()
    c.execute("INSERT INTO income (amount) VALUES (?)", (income,))
    c.execute("INSERT INTO expense (amount) VALUES (?)", (expense,))
    c.execute("INSERT INTO budget_goal (amount) VALUES (?)", (budget_goal,))
    conn.commit()
    conn.close()
    print("Data saved to the database!")

root = tk.Tk()
root.title("Budget App")

income_label = tk.Label(root, text="Income:")
income_label.grid(row=0, column=0)

income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1)

expense_label = tk.Label(root, text="Expense:")
expense_label.grid(row=1, column=0)

expense_entry = tk.Entry(root)
expense_entry.grid(row=1, column=1)

budget_goal_label = tk.Label(root, text="Budget Goal:")
budget_goal_label.grid(row=2, column=0)

budget_goal_entry = tk.Entry(root)
budget_goal_entry.grid(row=2, column=1)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2)

root.mainloop()



on_submit()
