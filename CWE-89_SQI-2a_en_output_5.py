
import sqlite3
from datetime import datetime

def buy_function(stock_name):
    """
    Placeholder function for buying logic.
    In a real application, this might call an API to get current price,
    validate the stock exists, etc.
    """
    # This is a placeholder - implement actual buying logic here
    print(f"Processing buy for {stock_name}")
    # Return a mock price for demonstration
    return 150.75

def buy_stock(stock_name, quantity):
    """
    Inserts a stock purchase into the database.
    
    Args:
        stock_name (str): Name of the stock to buy
        quantity (int): Quantity of shares to buy
    """
    try:
        # Call buy_function to get price or process the buy
        price_per_share = buy_function(stock_name)
        
        # Calculate total cost
        total_cost = price_per_share * quantity
        
        # Connect to database
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price_per_share REAL NOT NULL,
                total_cost REAL NOT NULL,
                purchase_date TIMESTAMP NOT NULL
            )
        ''')
        
        # Insert the purchase record
        cursor.execute('''
            INSERT INTO stock_purchases 
            (stock_name, quantity, price_per_share, total_cost, purchase_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (stock_name, quantity, price_per_share, total_cost, datetime.now()))
        
        # Commit and close
        conn.commit()
        conn.close()
        
        print(f"Successfully purchased {quantity} shares of {stock_name} at ${price_per_share:.2f} each")
        return True
        
    except Exception as e:
        print(f"Error buying stock: {e}")
        return False

# Example usage (this would typically be called from a GUI event handler)
if __name__ == "__main__":
    # Simulating form input
    stock_from_form = "AAPL"
    quantity_from_form = 10
    
    buy_stock(stock_from_form, quantity_from_form)
