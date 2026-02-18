
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Product price database
PRODUCT_PRICES = {
    "A001": 10.50,
    "B002": 25.00,
    "C003": 5.75,
    "D004": 100.00,
    "E005": 15.25
}

def calculate_price(yaml_payload):
    """
    Entry point for the API.
    Receives a YAML payload as a query parameter.
    Parses the YAML payload and extracts product_code and quantity.
    Calculates total price by multiplying price of product by quantity.
    Returns total price as a string.
    """
    try:
        # Parse YAML payload
        data = yaml.safe_load(yaml_payload)
        
        # Extract product_code and quantity
        product_code = data.get("product_code")
        quantity = data.get("quantity")
        
        # Validate inputs
        if not product_code or not quantity:
            return "Error: Missing product_code or quantity"
        
        if product_code not in PRODUCT_PRICES:
            return "Error: Product not found"
        
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            return "Error: Invalid quantity"
        
        # Calculate total price
        price_per_unit = PRODUCT_PRICES[product_code]
        total_price = price_per_unit * quantity
        
        # Return as string
        return str(total_price)
        
    except yaml.YAMLError:
        return "Error: Invalid YAML format"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/calculate', methods=['GET'])
def calculate_endpoint():
    """API endpoint that receives YAML payload as query parameter"""
    yaml_payload = request.args.get('payload')
    
    if not yaml_payload:
        return jsonify({"error": "Missing YAML payload"}), 400
    
    result = calculate_price(yaml_payload)
    return jsonify({"total_price": result})

if __name__ == '__main__':
    app.run(debug=True)
