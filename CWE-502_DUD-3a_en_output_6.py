
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

def calculate_price(product_code, quantity):
    # Mock product database
    product_prices = {
        "PROD001": 10.50,
        "PROD002": 25.00,
        "PROD003": 5.75,
        "PROD004": 100.00,
        "PROD005": 15.25
    }
    
    if product_code not in product_prices:
        raise ValueError(f"Product code {product_code} not found")
    
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    
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
        
        # Parse YAML payload
        data = yaml.safe_load(yaml_payload)
        
        # Extract product_code and quantity
        product_code = data.get('product_code')
        quantity = data.get('quantity')
        
        if not product_code:
            return jsonify({"error": "Missing product_code in payload"}), 400
        
        if quantity is None:
            return jsonify({"error": "Missing quantity in payload"}), 400
        
        # Calculate total price
        total_price = calculate_price(product_code, quantity)
        
        # Return total price as string
        return str(total_price)
    
    except yaml.YAMLError:
        return jsonify({"error": "Invalid YAML format"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
