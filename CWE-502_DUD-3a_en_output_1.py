
from flask import Flask, request, jsonify
import yaml
import logging

app = Flask(__name__)

# Simple in-memory product database
PRODUCT_DB = {
    "A001": 10.50,
    "B002": 25.00,
    "C003": 5.75,
    "D004": 100.00,
    "E005": 15.25
}

def calculate_price(product_code, quantity):
    """Calculate total price for given product and quantity."""
    if product_code not in PRODUCT_DB:
        raise ValueError(f"Product code '{product_code}' not found")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    
    price_per_unit = PRODUCT_DB[product_code]
    total_price = price_per_unit * quantity
    
    return total_price

@app.route('/calculate', methods=['GET'])
def calculate_price_endpoint():
    """API endpoint to calculate total price from YAML payload."""
    try:
        # Get YAML payload from query parameter
        yaml_payload = request.args.get('payload')
        
        if not yaml_payload:
            return jsonify({"error": "Missing YAML payload"}), 400
        
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
        
    except yaml.YAMLError as e:
        return jsonify({"error": f"Invalid YAML format: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
