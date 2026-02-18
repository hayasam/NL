
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

def calculate_price(product_code, quantity):
    # Mock product database
    product_prices = {
        "A001": 10.50,
        "B002": 25.00,
        "C003": 5.75,
        "D004": 100.00
    }
    
    if product_code not in product_prices:
        raise ValueError(f"Product code {product_code} not found")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    
    price = product_prices[product_code]
    total_price = price * quantity
    return total_price

@app.route('/calculate', methods=['GET'])
def calculate_price_api():
    try:
        # Get YAML payload from query parameter
        yaml_payload = request.args.get('payload')
        if not yaml_payload:
            return jsonify({"error": "Missing payload parameter"}), 400
        
        # Parse YAML
        data = yaml.safe_load(yaml_payload)
        
        # Extract product_code and quantity
        product_code = data.get('product_code')
        quantity = data.get('quantity')
        
        if not product_code:
            return jsonify({"error": "Missing product_code"}), 400
        if quantity is None:
            return jsonify({"error": "Missing quantity"}), 400
        
        # Calculate total price
        total_price = calculate_price(product_code, quantity)
        
        # Return total price as string
        return jsonify({"total_price": str(total_price)}), 200
    
    except yaml.YAMLError:
        return jsonify({"error": "Invalid YAML format"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
