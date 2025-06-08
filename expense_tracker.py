import sqlite3

# Connect to SQLite (creates DB if not exists)
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    note TEXT
)
""")
conn.commit()

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")
    
    cursor.execute("INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
                   (date, category, amount, note))
    conn.commit()
    print("✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("\n📋 All Expenses:\n")
    for row in rows:
        print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ₹{row[3]}, Note: {row[4]}")
    print()

# Function to show total expenses
def show_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    total = total if total else 0
    print(f"\n💰 Total Amount Spent: ₹{total:.2f}\n")

# Main menu
def main():
    while True:
        print("📊 Expense Tracker")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Show Total Expense")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
