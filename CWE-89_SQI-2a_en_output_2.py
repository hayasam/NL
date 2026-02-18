
import sqlite3
from datetime import datetime

def buy_stock(stock_name, quantity):
    try:
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                purchase_date TIMESTAMP NOT NULL
            )
        ''')
        
        purchase_date = datetime.now()
        cursor.execute('''
            INSERT INTO purchases (stock_name, quantity, purchase_date)
            VALUES (?, ?, ?)
        ''', (stock_name, quantity, purchase_date))
        
        conn.commit()
        conn.close()
        
        buy_function(stock_name)
        
        return True
    except Exception as e:
        print(f"Error buying stock: {e}")
        return False

def buy_function(stock_name):
    try:
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_actions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                action_type TEXT NOT NULL,
                action_date TIMESTAMP NOT NULL
            )
        ''')
        
        action_date = datetime.now()
        cursor.execute('''
            INSERT INTO stock_actions (stock_name, action_type, action_date)
            VALUES (?, 'BUY', ?)
        ''', (stock_name, action_date))
        
        conn.commit()
        conn.close()
        
        return True
    except Exception as e:
        print(f"Error in buy_function: {e}")
        return False
