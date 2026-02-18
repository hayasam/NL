
import sqlite3
from datetime import datetime

def buy_function(stock_name):
    """
    Placeholder function for buying logic.
    In a real application, this might call an API to get current price,
    validate the stock exists, etc.
    """
    # Example: Get current price from an API or database
    # current_price = get_stock_price(stock_name)
    # return current_price
    
    # For now, return a dummy price
    return 150.75

def buy_stock(stock_name, quantity):
    """
    Inserts a stock purchase into the database.
    
    Args:
        stock_name: Name of the stock to buy
        quantity: Number of shares to purchase
    """
    try:
        # Get current price using the buy_function
        price_per_share = buy_function(stock_name)
        total_cost = price_per_share * quantity
        purchase_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Connect to database
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price_per_share REAL NOT NULL,
                total_cost REAL NOT NULL,
                purchase_date TEXT NOT NULL
            )
        ''')
        
        # Insert the purchase record
        cursor.execute('''
            INSERT INTO purchases (stock_name, quantity, price_per_share, total_cost, purchase_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (stock_name, quantity, price_per_share, total_cost, purchase_date))
        
        # Commit and close
        conn.commit()
        conn.close()
        
        print(f"Successfully purchased {quantity} shares of {stock_name} at ${price_per_share:.2f} each")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage (this would typically be called from a GUI event handler)
# buy_stock("AAPL", 10)
