
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    payload_param = request.args.get('payload')
    
    if payload_param:
        try:
            import json
            payload_dict = json.loads(payload_param)
            name_value = payload_dict.get('name')
            return jsonify({'name': name_value})
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid JSON payload'}), 400
    else:
        return jsonify({'error': 'Missing payload parameter'}), 400

if __name__ == '__main__':
    app.run(debug=True)
