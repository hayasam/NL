
import sqlite3
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('weather.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        date = request.args.get('date')
        
        if not latitude or not longitude or not date:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT temperature 
        FROM weather_data 
        WHERE latitude = ? AND longitude = ? AND date = ?
        """
        
        cursor.execute(query, (latitude, longitude, date))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            return jsonify({'temperature': result['temperature']})
        else:
            return jsonify({'error': 'No data found for the given parameters'}), 404
            
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
