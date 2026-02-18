
from flask import Flask, request, jsonify
import yaml
import re

app = Flask(__name__)

# Product price catalog
PRODUCT_PRICES = {
    "A001": 10.50,
    "B002": 25.00,
    "C003": 5.75,
    "D004": 100.00,
    "E005": 15.25
}

def parse_yaml_payload(yaml_string):
    """Parse YAML payload and extract product_code and quantity."""
    try:
        data = yaml.safe_load(yaml_string)
        if not data:
            raise ValueError("Empty YAML payload")
        
        product_code = data.get("product_code")
        quantity = data.get("quantity")
        
        if product_code is None or quantity is None:
            raise ValueError("Missing required fields: product_code or quantity")
        
        if not isinstance(product_code, str):
            raise ValueError("product_code must be a string")
        
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("quantity must be a positive number")
        
        return product_code, float(quantity)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format: {str(e)}")

def calculate_price(product_code, quantity):
    """Calculate total price for given product and quantity."""
    if product_code not in PRODUCT_PRICES:
        raise ValueError(f"Product code '{product_code}' not found")
    
    price_per_unit = PRODUCT_PRICES[product_code]
    total_price = price_per_unit * quantity
    
    # Round to 2 decimal places for currency
    return round(total_price, 2)

@app.route('/calculate_price', methods=['GET'])
def calculate_price_endpoint():
    """API endpoint to calculate price from YAML payload."""
    try:
        # Get YAML payload from query parameter
        yaml_payload = request.args.get('payload')
        
        if not yaml_payload:
            return jsonify({"error": "Missing 'payload' query parameter"}), 400
        
        # Parse YAML and extract data
        product_code, quantity = parse_yaml_payload(yaml_payload)
        
        # Calculate total price
        total_price = calculate_price(product_code, quantity)
        
        # Return as string as specified
        return str(total_price)
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
