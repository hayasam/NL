
from flask import Flask, request, jsonify
import yaml
import logging

app = Flask(__name__)

# Simple in-memory product database
PRODUCT_DB = {
    "A001": 10.50,
    "B002": 25.00,
    "C003": 5.75,
    "D004": 100.00
}

def calculate_price(product_code, quantity):
    """Calculate total price for given product and quantity."""
    if product_code not in PRODUCT_DB:
        raise ValueError(f"Product code '{product_code}' not found")
    
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    
    price = PRODUCT_DB[product_code]
    total = price * quantity
    return total

@app.route('/calculate', methods=['GET'])
def calculate_price_api():
    """API endpoint to calculate price from YAML payload."""
    try:
        # Get YAML payload from query parameter
        yaml_payload = request.args.get('payload')
        
        if not yaml_payload:
            return jsonify({"error": "Missing YAML payload"}), 400
        
        # Parse YAML
        data = yaml.safe_load(yaml_payload)
        
        # Extract required fields
        product_code = data.get('product_code')
        quantity = data.get('quantity')
        
        if not product_code:
            return jsonify({"error": "Missing product_code"}), 400
        
        if quantity is None:
            return jsonify({"error": "Missing quantity"}), 400
        
        # Calculate price
        total_price = calculate_price(product_code, quantity)
        
        # Return total price as string
        return str(total_price), 200
        
    except yaml.YAMLError as e:
        return jsonify({"error": f"Invalid YAML format: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.exception("Unexpected error occurred")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
