
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Sample product database
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
        data = yaml.safe_load(yaml_payload)
        product_code = data.get("product_code")
        quantity = data.get("quantity")
        
        if not product_code or not quantity:
            return "Error: Missing product_code or quantity"
        
        if product_code not in PRODUCTS:
            return "Error: Product not found"
        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                return "Error: Quantity must be positive"
        except ValueError:
            return "Error: Quantity must be an integer"
        
        price = PRODUCTS[product_code]
        total_price = price * quantity
        
        return str(total_price)
    
    except yaml.YAMLError:
        return "Error: Invalid YAML format"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/calculate', methods=['GET'])
def calculate_price_api():
    """
    API endpoint that receives YAML payload as query parameter.
    """
    yaml_payload = request.args.get('payload')
    
    if not yaml_payload:
        return jsonify({"error": "Missing YAML payload"}), 400
    
    result = calculate_price(yaml_payload)
    
    if result.startswith("Error:"):
        return jsonify({"error": result}), 400
    
    return jsonify({"total_price": result})

if __name__ == '__main__':
    app.run(debug=True)
