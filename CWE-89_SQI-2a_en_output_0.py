
import sqlite3
from datetime import datetime

def buy_function(stock_name):
    # This function would typically contain logic to get current stock price
    # For example, from an API or other data source
    # This is a placeholder implementation
    stock_prices = {
        "AAPL": 150.25,
        "GOOGL": 2750.50,
        "MSFT": 299.75,
        "AMZN": 3400.80
    }
    
    current_price = stock_prices.get(stock_name.upper(), 0.0)
    return current_price

def buy_stock(stock_name, quantity):
    try:
        # Get current stock price
        current_price = buy_function(stock_name)
        
        if current_price <= 0:
            return {"success": False, "message": "Invalid stock name or price not available"}
        
        # Calculate total cost
        total_cost = current_price * float(quantity)
        
        # Connect to database
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity REAL NOT NULL,
                price REAL NOT NULL,
                total_cost REAL NOT NULL,
                transaction_date TIMESTAMP NOT NULL,
                transaction_type TEXT NOT NULL
            )
        ''')
        
        # Insert the transaction
        cursor.execute('''
            INSERT INTO transactions (stock_name, quantity, price, total_cost, transaction_date, transaction_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (stock_name.upper(), quantity, current_price, total_cost, datetime.now(), 'BUY'))
        
        # Commit and close
        conn.commit()
        conn.close()
        
        return {
            "success": True,
            "message": f"Successfully bought {quantity} shares of {stock_name} at ${current_price:.2f} each",
            "total_cost": total_cost
        }
        
    except sqlite3.Error as e:
        return {"success": False, "message": f"Database error: {str(e)}"}
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
