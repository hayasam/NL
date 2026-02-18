
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  stock_name TEXT NOT NULL,
                  quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('order_form.html')

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    quantity = request.form['quantity']
    
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders (stock_name, quantity) VALUES (?, ?)",
              (stock_name, quantity))
    conn.commit()
    conn.close()
    
    return redirect(url_for('stock_view'))

@app.route('/stock_view')
def stock_view():
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    orders = c.fetchall()
    conn.close()
    
    return render_template('stock_view.html', orders=orders)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
