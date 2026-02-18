
import sqlite3
from datetime import datetime

def buy_function(stock_name):
    # This function would typically contain logic for the actual purchase
    # For example: API call to trading platform, price validation, etc.
    # This is a placeholder implementation
    print(f"Processing purchase for {stock_name}")
    # Return a mock transaction ID or actual result
    return f"TX-{datetime.now().strftime('%Y%m%d%H%M%S')}"

def buy_stock(stock_name, quantity):
    try:
        # Connect to database
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                transaction_id TEXT
            )
        ''')
        
        # Call buy_function to process the purchase
        transaction_id = buy_function(stock_name)
        
        # Insert purchase into database
        cursor.execute('''
            INSERT INTO purchases (stock_name, quantity, transaction_id)
            VALUES (?, ?, ?)
        ''', (stock_name, quantity, transaction_id))
        
        # Commit the transaction
        conn.commit()
        
        print(f"Successfully purchased {quantity} shares of {stock_name}")
        return True
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False
        
    finally:
        if conn:
            conn.close()
