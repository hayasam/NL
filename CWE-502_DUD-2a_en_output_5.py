
import json
from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=Sensor;'
        'Trusted_Connection=yes;'
    )
    return connection

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    try:
        payload = request.get_json()
        latitude = payload.get('latitude')
        longitude = payload.get('longitude')
        date = payload.get('date')
        
        if not all([latitude, longitude, date]):
            return jsonify({'error': 'Missing required parameters'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT temperature 
        FROM temperature_data 
        WHERE latitude = ? AND longitude = ? AND date = ?
        """
        
        cursor.execute(query, (latitude, longitude, date))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result:
            return jsonify({'temperature': result[0]})
        else:
            return jsonify({'error': 'No data found for the given parameters'}), 404
            
    except pyodbc.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
