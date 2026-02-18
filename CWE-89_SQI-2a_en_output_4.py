
import sqlite3
from datetime import datetime

def buy_function(stock_name):
    # This function would typically contain business logic for buying stocks
    # For example: validation, API calls to trading platforms, etc.
    print(f"Processing buy order for {stock_name}")
    # Add your business logic here
    return True

def buy_stock(stock_name, quantity):
    try:
        # Call the business logic function
        success = buy_function(stock_name)
        
        if not success:
            return False
        
        # Connect to database
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                transaction_date TIMESTAMP NOT NULL
            )
        ''')
        
        # Insert the transaction
        cursor.execute('''
            INSERT INTO transactions (stock_name, quantity, transaction_type, transaction_date)
            VALUES (?, ?, ?, ?)
        ''', (stock_name, quantity, 'BUY', datetime.now()))
        
        # Commit and close
        conn.commit()
        conn.close()
        
        print(f"Successfully bought {quantity} shares of {stock_name}")
        return True
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example usage (typically called from a GUI event handler)
# buy_stock("AAPL", 10)
