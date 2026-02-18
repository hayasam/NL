
import json
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Sensor',
            user='your_username',
            password='your_password'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    try:
        payload = request.get_json()
        
        if not payload:
            return jsonify({'error': 'No payload provided'}), 400
        
        latitude = payload.get('latitude')
        longitude = payload.get('longitude')
        date = payload.get('date')
        
        if latitude is None or longitude is None or date is None:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        connection = create_db_connection()
        if connection is None:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT temperature 
        FROM temperature_data 
        WHERE latitude = %s AND longitude = %s AND date = %s
        """
        
        cursor.execute(query, (latitude, longitude, date))
        result = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        if result:
            return jsonify({'temperature': result['temperature']}), 200
        else:
            return jsonify({'error': 'No temperature data found for the given location and date'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
