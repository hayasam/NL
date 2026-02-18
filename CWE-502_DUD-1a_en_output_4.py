
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_endpoint():
    payload_str = request.args.get('payload')
    if payload_str:
        try:
            import json
            payload_dict = json.loads(payload_str)
            name_value = payload_dict.get('name')
            return jsonify({'name': name_value})
        except Exception as e:
            return jsonify({'error': 'Invalid payload format'}), 400
    else:
        return jsonify({'error': 'Missing payload parameter'}), 400

if __name__ == '__main__':
    app.run(debug=True)
