
import yaml
from flask import Flask, request

app = Flask(__name__)

def get_price_for_product_code(product_code):
    # Mock implementation - replace with actual logic
    prices = {
        "A001": 10.50,
        "B002": 25.00,
        "C003": 5.75
    }
    return prices.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')
    
    if not yaml_payload:
        return yaml.dump({"error": "No YAML payload provided"}), 400
    
    try:
        data = yaml.safe_load(yaml_payload)
        
        product_code = data.get('product_code')
        quantity = data.get('quantity', 1)
        
        if not product_code:
            return yaml.dump({"error": "Product code is required"}), 400
        
        unit_price = get_price_for_product_code(product_code)
        
        if unit_price == 0.0:
            return yaml.dump({"error": f"Product code {product_code} not found"}), 404
        
        total_price = unit_price * quantity
        
        response = {
            "product_code": product_code,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        }
        
        return yaml.dump(response), 200
        
    except yaml.YAMLError:
        return yaml.dump({"error": "Invalid YAML format"}), 400
    except Exception as e:
        return yaml.dump({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
