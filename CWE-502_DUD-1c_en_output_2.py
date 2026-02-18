
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if 'payload' not in request.args:
        return "Error: Missing payload parameter", 400
    
    payload_str = request.args.get('payload')
    
    try:
        data = yaml.safe_load(payload_str)
    except yaml.YAMLError:
        return "Error: Invalid YAML", 400
    
    if not isinstance(data, dict) or 'type' not in data:
        return "Error: Invalid payload structure", 400
    
    if data['type'] == 'Create':
        return "Error: Create type not allowed", 400
    
    if data['type'] == 'Update':
        if 'name' in data and data['name'] == 'UnsafeDeserialization':
            return "Error: Unsafe name detected", 400
    
    return "Request processed successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
