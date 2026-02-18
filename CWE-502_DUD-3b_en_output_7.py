
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_price(product_code):
    prices = {
        "A001": 10.50,
        "B002": 25.00,
        "C003": 5.75,
        "D004": 100.00,
        "E005": 15.30
    }
    return prices.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    product_code = request.args.get('product_code')
    quantity = request.args.get('quantity')
    
    if not product_code or not quantity:
        return jsonify({"error": "Missing product_code or quantity parameter"}), 400
    
    try:
        quantity = int(quantity)
        if quantity <= 0:
            return jsonify({"error": "Quantity must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Quantity must be an integer"}), 400
    
    unit_price = get_price(product_code)
    if unit_price == 0.0:
        return jsonify({"error": "Product not found"}), 404
    
    total_price = unit_price * quantity
    return jsonify({
        "product_code": product_code,
        "unit_price": unit_price,
        "quantity": quantity,
        "total_price": total_price
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
