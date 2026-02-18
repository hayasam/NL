
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_product_price(product_code):
    price_map = {
        "A001": 10.50,
        "B002": 25.00,
        "C003": 5.75,
        "D004": 100.00,
        "E005": 15.25
    }
    return price_map.get(product_code, None)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    product_code = request.args.get('product_code')
    quantity_str = request.args.get('quantity')
    
    if not product_code or not quantity_str:
        return jsonify({"error": "Missing product_code or quantity parameter"}), 400
    
    try:
        quantity = int(quantity_str)
        if quantity <= 0:
            return jsonify({"error": "Quantity must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Quantity must be an integer"}), 400
    
    price = get_product_price(product_code)
    
    if price is None:
        return jsonify({"error": "Product code not found"}), 404
    
    total_price = price * quantity
    return jsonify({
        "product_code": product_code,
        "unit_price": price,
        "quantity": quantity,
        "total_price": round(total_price, 2)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
