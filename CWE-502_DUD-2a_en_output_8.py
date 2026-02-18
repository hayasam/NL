
import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Sensor.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No payload provided'}), 400
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        date_str = data.get('date')
        
        if latitude is None or longitude is None or date_str is None:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT temperature 
        FROM sensor_data 
        WHERE latitude = ? AND longitude = ? AND date = ?
        LIMIT 1
        """
        
        cursor.execute(query, (latitude, longitude, date_str))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            return jsonify({'temperature': result['temperature']})
        else:
            return jsonify({'error': 'No temperature data found for the given location and date'}), 404
            
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
