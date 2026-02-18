
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class StockOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def order_form():
    return render_template('order_form.html')

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    quantity = request.form['quantity']
    
    new_order = StockOrder(stock_name=stock_name, quantity=quantity)
    db.session.add(new_order)
    db.session.commit()
    
    return redirect(url_for('stock_view'))

@app.route('/stock_view')
def stock_view():
    orders = StockOrder.query.all()
    return render_template('stock_view.html', orders=orders)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
