
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_name', methods=['POST'])
def check_name():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON payload provided'}), 400
        
        if 'name' in data:
            return jsonify({'name': data['name']}), 200
        else:
            return jsonify({'error': 'Field "name" not found in payload'}), 400
            
    except Exception as e:
        return jsonify({'error': f'Invalid request: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)
