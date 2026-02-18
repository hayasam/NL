
from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/buy', methods=['POST'])
def buy_stock():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = request.form.get('username')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO orders (username, stock_name, quantity, order_type)
        VALUES (?, ?, ?, 'buy')
    ''', (username, stock_name, stock_quantity))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('profile', username=username))

if __name__ == '__main__':
    app.run(debug=True)
