
import sqlite3
from datetime import datetime

def buy_function(stock_name):
    # This function would typically fetch current stock price from an API
    # For this example, we'll return a mock price
    mock_prices = {
        "AAPL": 175.25,
        "GOOGL": 135.50,
        "TSLA": 210.75,
        "MSFT": 330.10
    }
    return mock_prices.get(stock_name, 100.00)

def buy_stock(stock_name, quantity):
    try:
        # Get current stock price
        current_price = buy_function(stock_name)
        
        # Calculate total cost
        total_cost = current_price * quantity
        
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Connect to database
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                total_cost REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        
        # Insert transaction into database
        cursor.execute('''
            INSERT INTO transactions (stock_name, quantity, price, total_cost, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (stock_name, quantity, current_price, total_cost, timestamp))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        return True, f"Successfully bought {quantity} shares of {stock_name} at ${current_price:.2f} each"
        
    except Exception as e:
        return False, f"Error buying stock: {str(e)}"
