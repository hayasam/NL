
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

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
        date_str = request.args.get('date')
        
        if not all([latitude, longitude, date_str]):
            return jsonify({'error': 'Missing required parameters'}), 400
        
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT temperature 
        FROM weather_data 
        WHERE latitude = ? AND longitude = ? AND date = ?
        """
        
        cursor.execute(query, (float(latitude), float(longitude), date_str))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            return jsonify({'temperature': result['temperature']})
        else:
            return jsonify({'error': 'No data found for the specified location and date'}), 404
            
    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
