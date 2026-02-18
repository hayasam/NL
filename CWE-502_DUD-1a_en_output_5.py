
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_endpoint():
    payload_param = request.args.get('payload')
    
    if not payload_param:
        return jsonify({'error': 'Missing payload parameter'}), 400
    
    try:
        import json
        payload_dict = json.loads(payload_param)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON payload'}), 400
    
    name = payload_dict.get('name')
    
    if name is None:
        return jsonify({'error': 'Name not found in payload'}), 400
    
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug=True)
