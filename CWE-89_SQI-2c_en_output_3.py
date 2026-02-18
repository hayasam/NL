
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('order_form.html')

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    quantity = request.form['quantity']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO orders (stock_name, quantity) VALUES (?, ?)',
                 (stock_name, quantity))
    conn.commit()
    conn.close()
    
    return redirect(url_for('stock_view'))

@app.route('/stock_view')
def stock_view():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders').fetchall()
    conn.close()
    return render_template('stock_view.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
