
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Mock product database
PRODUCTS = {
    "A001": 10.50,
    "B002": 25.00,
    "C003": 5.75,
    "D004": 100.00
}

def calculate_price(yaml_payload):
    """
    Calculate total price from YAML payload containing product_code and quantity.
    """
    try:
        # Parse YAML payload
        data = yaml.safe_load(yaml_payload)
        
        # Extract product_code and quantity
        product_code = data.get('product_code')
        quantity = data.get('quantity')
        
        # Validate inputs
        if not product_code or not quantity:
            return jsonify({'error': 'Missing product_code or quantity'}), 400
        
        if product_code not in PRODUCTS:
            return jsonify({'error': 'Product not found'}), 404
        
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            return jsonify({'error': 'Quantity must be a positive number'}), 400
        
        # Calculate total price
        unit_price = PRODUCTS[product_code]
        total_price = unit_price * quantity
        
        # Return total price as string
        return jsonify({'total_price': str(total_price)}), 200
    
    except yaml.YAMLError:
        return jsonify({'error': 'Invalid YAML format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/calculate', methods=['GET'])
def calculate_price_api():
    """
    API endpoint that receives YAML payload as query parameter.
    """
    yaml_payload = request.args.get('payload')
    
    if not yaml_payload:
        return jsonify({'error': 'Missing YAML payload'}), 400
    
    return calculate_price(yaml_payload)

if __name__ == '__main__':
    app.run(debug=True)
